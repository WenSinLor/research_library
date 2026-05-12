#!/usr/bin/env python3
"""
generate_viz.py — research_library root

Usage:  python3 generate_viz.py

Scans ALL subdirectories under Research_Topics/, collects every paper that
has a .md file with YAML frontmatter, and writes research_library_viz.html
to the repo root, then opens it in the default browser.
"""

import re
import json
import datetime
import webbrowser
import yaml
from pathlib import Path

ROOT       = Path(__file__).parent
TOPICS_DIR = ROOT / "Research_Topics"
OUT_FILE   = ROOT / "research_library_viz.html"


# ── Data collection ───────────────────────────────────────────────────────────

def parse_md(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)", text, re.DOTALL)
    if not m:
        return None
    try:
        meta = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None
    if not isinstance(meta, dict):
        return None
    meta["body"] = m.group(2).strip()
    meta.setdefault("tags", [])
    meta["tags"] = [str(t) for t in (meta["tags"] or [])]
    for k in ("title", "authors", "year", "paper_type", "read_status", "citation_key"):
        meta.setdefault(k, "")
    for k, v in list(meta.items()):
        if isinstance(v, (datetime.date, datetime.datetime)):
            meta[k] = str(v)
    return meta


def collect_all() -> list[dict]:
    papers = []
    for topic_dir in sorted(TOPICS_DIR.iterdir()):
        if not topic_dir.is_dir():
            continue
        topic_name = topic_dir.name.replace("_", " ")
        for subdir in sorted(topic_dir.iterdir()):
            if not subdir.is_dir():
                continue
            md_files = list(subdir.glob("*.md"))
            if not md_files:
                continue
            data = parse_md(md_files[0])
            if data:
                data["topic"] = topic_name
                papers.append(data)
    papers.sort(
        key=lambda p: int(str(p["year"])) if str(p["year"]).isdigit() else 0,
        reverse=True,
    )
    return papers


# ── Minimal Markdown → HTML ───────────────────────────────────────────────────

def md_to_html(text: str) -> str:
    lines = text.split("\n")
    out, in_ul = [], False
    for line in lines:
        s = line.rstrip()
        if re.match(r"^## ", s):
            if in_ul: out.append("</ul>"); in_ul = False
            out.append(f"<h3>{s[3:].strip()}</h3>")
        elif re.match(r"^# ", s):
            if in_ul: out.append("</ul>"); in_ul = False
            out.append(f"<h2>{s[2:].strip()}</h2>")
        elif re.match(r"^[-*] ", s):
            if not in_ul: out.append("<ul>"); in_ul = True
            out.append(f"<li>{s[2:].strip()}</li>")
        elif s == "":
            if in_ul: out.append("</ul>"); in_ul = False
            out.append("<br>")
        else:
            if in_ul: out.append("</ul>"); in_ul = False
            out.append(f"<p>{s}</p>")
    if in_ul:
        out.append("</ul>")
    return "\n".join(out)


# ── HTML template ─────────────────────────────────────────────────────────────

HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Research Library — Paper Visualization</title>
<style>
/* ── VT Design Tokens ──────────────────────────────────────── */
:root {
  --vt-maroon:       #861F41;
  --vt-maroon-dark:  #5C1530;
  --vt-maroon-light: #A8304F;
  --vt-orange:       #E5751F;
  --vt-stone:        #75787B;
  --vt-stone-light:  #BEBFC0;
  --vt-stone-xlt:    #F2F0EF;
  --vt-white:        #FFFFFF;
  --vt-black:        #1A1A1A;
  --vt-blue:         #4A7FB5;
  --vt-teal:         #2E7D78;
  --radius:          6px;
  --shadow:          0 2px 10px rgba(0,0,0,.13);
  --transition:      .17s ease;
}

*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{
  font-family:'Segoe UI',system-ui,-apple-system,sans-serif;
  font-size:14px;background:var(--vt-stone-xlt);color:var(--vt-black);min-height:100vh;
}

/* ── Header ─────────────────────────────────────────────────── */
header{
  background:linear-gradient(135deg,var(--vt-maroon-dark) 0%,var(--vt-maroon) 55%,var(--vt-maroon-light) 100%);
  color:var(--vt-white);padding:26px 40px 22px;box-shadow:0 3px 14px rgba(0,0,0,.28);
}
.header-accent{display:inline-block;width:36px;height:4px;background:var(--vt-orange);border-radius:2px;margin-bottom:10px;}
header h1{font-size:1.55rem;font-weight:700;letter-spacing:.02em;}
header p.subtitle{margin-top:4px;font-size:.88rem;opacity:.82;}

/* ── Stats / Topic bar ──────────────────────────────────────── */
.stats-bar{
  display:flex;flex-wrap:wrap;gap:8px;
  padding:12px 40px;background:var(--vt-maroon-dark);
  align-items:center;
}
.bar-divider{width:1px;height:22px;background:rgba(255,255,255,.2);margin:0 4px;}
.bar-label{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:rgba(255,255,255,.5);}
.stat-chip{
  display:flex;align-items:center;gap:6px;
  background:rgba(255,255,255,.1);color:var(--vt-white);
  padding:4px 12px;border-radius:20px;font-size:.78rem;font-weight:600;
  cursor:pointer;transition:background var(--transition);user-select:none;
}
.stat-chip:hover{background:rgba(255,255,255,.22);}
.stat-chip.active-filter{background:var(--vt-orange) !important;}
.stat-chip .dot{width:8px;height:8px;border-radius:50%;flex-shrink:0;}

/* ── Controls ───────────────────────────────────────────────── */
.controls{
  padding:16px 40px;background:var(--vt-white);
  border-bottom:1px solid var(--vt-stone-light);
  display:flex;flex-wrap:wrap;gap:14px;align-items:flex-end;
}
.control-group{display:flex;flex-direction:column;gap:5px;}
.control-group label{
  font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;color:var(--vt-stone);
}
input[type="text"],select{
  padding:7px 12px;border:1.5px solid var(--vt-stone-light);border-radius:var(--radius);
  font-size:.875rem;background:var(--vt-white);color:var(--vt-black);
  transition:border-color var(--transition),box-shadow var(--transition);outline:none;
}
input[type="text"]:focus,select:focus{
  border-color:var(--vt-maroon);box-shadow:0 0 0 3px rgba(134,31,65,.12);
}
input[type="text"]{min-width:260px;}
select{min-width:150px;cursor:pointer;}

.filter-tags{display:flex;flex-wrap:wrap;gap:5px;max-width:700px;}
.filter-tag{
  padding:3px 10px;border-radius:20px;border:1.5px solid var(--vt-stone-light);
  background:var(--vt-white);font-size:.72rem;font-weight:700;
  cursor:pointer;transition:all var(--transition);user-select:none;color:var(--vt-stone);
}
.filter-tag:hover{border-color:var(--vt-maroon);color:var(--vt-maroon);}
.filter-tag.active{background:var(--vt-maroon);border-color:var(--vt-maroon);color:var(--vt-white);}

.btn-reset{
  padding:7px 16px;border-radius:var(--radius);border:1.5px solid var(--vt-orange);
  background:transparent;color:var(--vt-orange);font-size:.875rem;font-weight:600;
  cursor:pointer;transition:all var(--transition);height:34px;align-self:flex-end;
}
.btn-reset:hover{background:var(--vt-orange);color:var(--vt-white);}
.results-count{align-self:flex-end;padding-bottom:2px;font-size:.8rem;color:var(--vt-stone);}

/* ── Table ──────────────────────────────────────────────────── */
.table-wrap{padding:20px 40px 48px;overflow-x:auto;}
table{
  width:100%;border-collapse:separate;border-spacing:0;
  background:var(--vt-white);border-radius:10px;box-shadow:var(--shadow);overflow:hidden;
}
thead th{
  background:var(--vt-maroon);color:var(--vt-white);padding:11px 14px;
  font-size:.76rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em;
  white-space:nowrap;user-select:none;cursor:pointer;
  position:sticky;top:0;z-index:2;
  border-right:1px solid var(--vt-maroon-dark);transition:background var(--transition);
}
thead th:last-child{border-right:none;}
thead th:hover{background:var(--vt-maroon-light);}
.sort-icon{margin-left:4px;opacity:.55;font-size:.68rem;}
thead th.sorted-asc  .sort-icon::after{content:" ▲";opacity:1;}
thead th.sorted-desc .sort-icon::after{content:" ▼";opacity:1;}
thead th:not(.sorted-asc):not(.sorted-desc) .sort-icon::after{content:" ⇅";}

tbody tr.paper-row{cursor:pointer;transition:background var(--transition);border-bottom:1px solid #f0eeed;}
tbody tr.paper-row:hover{background:#fdf5f6;}
tbody tr.paper-row.expanded{background:#fdf0f3;}
tbody td{padding:10px 14px;vertical-align:middle;font-size:.83rem;border-right:1px solid #f0eeed;}
tbody td:last-child{border-right:none;}

/* ── Detail row ─────────────────────────────────────────────── */
tr.detail-row td{padding:0;background:#fff8f9;border-bottom:2px solid var(--vt-maroon);}
.detail-inner{
  display:grid;grid-template-columns:1fr 1fr;gap:0 32px;
  padding:20px 32px;max-height:440px;overflow-y:auto;
}
.detail-inner h2{
  font-size:.95rem;color:var(--vt-maroon);margin-bottom:6px;padding-bottom:4px;
  border-bottom:2px solid var(--vt-orange);grid-column:1/-1;
}
.detail-inner h3{
  font-size:.78rem;font-weight:700;color:var(--vt-maroon);
  margin-top:12px;margin-bottom:4px;text-transform:uppercase;letter-spacing:.05em;
}
.detail-inner p{font-size:.84rem;line-height:1.65;color:#333;margin-bottom:6px;}
.detail-inner ul{padding-left:18px;margin-bottom:6px;}
.detail-inner li{font-size:.84rem;line-height:1.6;color:#333;}

/* ── Expand button ──────────────────────────────────────────── */
.expand-btn{
  width:21px;height:21px;border-radius:50%;
  background:var(--vt-stone-xlt);border:1.5px solid var(--vt-stone-light);
  display:inline-flex;align-items:center;justify-content:center;
  font-size:.7rem;color:var(--vt-stone);transition:all var(--transition);flex-shrink:0;
}
tr.expanded .expand-btn{
  background:var(--vt-maroon);border-color:var(--vt-maroon);color:var(--vt-white);transform:rotate(45deg);
}

/* ── Cell styles ─────────────────────────────────────────────── */
.cite-key{font-family:'Courier New',monospace;font-size:.77rem;color:var(--vt-maroon);font-weight:700;white-space:nowrap;}
.paper-title{font-size:.85rem;font-weight:600;line-height:1.35;max-width:320px;}
.year-badge{
  display:inline-block;background:var(--vt-stone-xlt);border:1px solid var(--vt-stone-light);
  color:var(--vt-black);padding:2px 8px;border-radius:var(--radius);font-size:.77rem;font-weight:700;white-space:nowrap;
}

/* ── Topic badge ────────────────────────────────────────────── */
.topic-badge{
  display:inline-block;padding:3px 10px;border-radius:20px;
  font-size:.72rem;font-weight:700;white-space:nowrap;cursor:pointer;
  transition:opacity var(--transition);
}
.topic-badge:hover{opacity:.75;}

/* ── Type badges ────────────────────────────────────────────── */
.type-badge{
  display:inline-flex;align-items:center;gap:5px;padding:3px 10px;border-radius:20px;
  font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;white-space:nowrap;
}
.type-theory    {background:#f5e9ec;color:var(--vt-maroon);border:1px solid #d4a0b0;}
.type-experiment{background:#fef0e4;color:#b85500;border:1px solid #f0c090;}
.type-simulation{background:#e8f1f9;color:#2d5f8a;border:1px solid #9bbdd9;}
.type-review    {background:#e6f4f3;color:var(--vt-teal);border:1px solid #9dd0cb;}

/* ── Status badges ──────────────────────────────────────────── */
.status-badge{
  display:inline-block;padding:2px 8px;border-radius:20px;
  font-size:.71rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;white-space:nowrap;
}
.status-read   {background:#e8f5e9;color:#2e7d32;border:1px solid #a5d6a7;}
.status-skimmed{background:#fff8e1;color:#f57f17;border:1px solid #ffe082;}
.status-unread {background:#f3f3f3;color:var(--vt-stone);border:1px solid #ddd;}

/* ── Tags ────────────────────────────────────────────────────── */
.tags-cell{display:flex;flex-wrap:wrap;gap:4px;max-width:240px;}
.tag{
  display:inline-block;padding:2px 8px;border-radius:20px;
  font-size:.68rem;font-weight:600;white-space:nowrap;
  cursor:pointer;transition:opacity var(--transition);
}
.tag:hover{opacity:.72;}
.tag-prc  {background:#f0e6ea;color:var(--vt-maroon);border:1px solid #d4a0b0;}
.tag-rc   {background:#fdeee3;color:#b85500;border:1px solid #f0c090;}
.tag-dyn  {background:#e8f1f9;color:#2d5f8a;border:1px solid #9bbdd9;}
.tag-emb  {background:#e6f4f3;color:var(--vt-teal);border:1px solid #9dd0cb;}
.tag-mem  {background:#f3eafc;color:#6a3fa3;border:1px solid #c9a8e8;}
.tag-neuro{background:#e8f5e9;color:#2e7d32;border:1px solid #a5d6a7;}
.tag-other{background:#f3f3f3;color:#555;border:1px solid #ddd;}

.no-results{text-align:center;padding:60px 20px;color:var(--vt-stone);font-size:.95rem;}

::-webkit-scrollbar{width:6px;height:6px;}
::-webkit-scrollbar-track{background:#f1f1f1;}
::-webkit-scrollbar-thumb{background:var(--vt-stone-light);border-radius:3px;}
::-webkit-scrollbar-thumb:hover{background:var(--vt-maroon);}

@media(max-width:900px){
  header,.stats-bar,.controls,.table-wrap{padding-left:16px;padding-right:16px;}
  .detail-inner{grid-template-columns:1fr;}
  input[type="text"]{min-width:180px;}
}
</style>
</head>
<body>

<header>
  <div class="header-accent"></div>
  <h1>Research Library</h1>
  <p class="subtitle">All topics &mdash; <span id="total-count"></span> papers</p>
</header>

<!-- Topic chips + type chips -->
<div class="stats-bar" id="stats-bar"></div>

<div class="controls">
  <div class="control-group">
    <label>Search</label>
    <input type="text" id="search" placeholder="Title, author, citation key&hellip;" oninput="applyFilters()">
  </div>
  <div class="control-group">
    <label>Year</label>
    <select id="year-filter" onchange="applyFilters()">
      <option value="">All years</option>
    </select>
  </div>
  <div class="control-group">
    <label>Read Status</label>
    <select id="status-filter" onchange="applyFilters()">
      <option value="">All statuses</option>
      <option value="read">Read</option>
      <option value="skimmed">Skimmed</option>
      <option value="unread">Unread</option>
    </select>
  </div>
  <div class="control-group" style="flex:1;min-width:220px;">
    <label>Filter by Tag</label>
    <div class="filter-tags" id="tag-filters"></div>
  </div>
  <button class="btn-reset" onclick="resetFilters()">Reset all</button>
  <span class="results-count" id="results-count"></span>
</div>

<div class="table-wrap">
<table id="papers-table">
  <thead><tr>
    <th style="width:36px;cursor:default;"></th>
    <th onclick="sortBy(1)">Citation Key<span class="sort-icon"></span></th>
    <th onclick="sortBy(2)">Title<span class="sort-icon"></span></th>
    <th onclick="sortBy(3)">Authors<span class="sort-icon"></span></th>
    <th onclick="sortBy(4)">Year<span class="sort-icon"></span></th>
    <th onclick="sortBy(5)">Topic<span class="sort-icon"></span></th>
    <th onclick="sortBy(6)">Type<span class="sort-icon"></span></th>
    <th onclick="sortBy(7)">Status<span class="sort-icon"></span></th>
    <th style="cursor:default;">Tags</th>
  </tr></thead>
  <tbody id="tbody"></tbody>
</table>
<div class="no-results" id="no-results" style="display:none;">No papers match the current filters.</div>
</div>

<script>
const PAPERS = __PAPERS_JSON__;

// ── Topic colour palette (VT-inspired) ───────────────────────
const TOPIC_PALETTES = [
  {bg:'#f5e9ec',color:'#861F41',border:'#d4a0b0',dot:'#861F41'},   // maroon
  {bg:'#fef0e4',color:'#b85500',border:'#f0c090',dot:'#E5751F'},   // orange
  {bg:'#e8f1f9',color:'#2d5f8a',border:'#9bbdd9',dot:'#4A7FB5'},   // blue
  {bg:'#e6f4f3',color:'#2E7D78',border:'#9dd0cb',dot:'#2E7D78'},   // teal
  {bg:'#f3eafc',color:'#6a3fa3',border:'#c9a8e8',dot:'#8B5CF6'},   // purple
  {bg:'#e8f5e9',color:'#2e7d32',border:'#a5d6a7',dot:'#2e7d32'},   // green
];
const ALL_TOPICS = [...new Set(PAPERS.map(p=>p.topic))].sort();
const TOPIC_PAL  = Object.fromEntries(ALL_TOPICS.map((t,i)=>[t, TOPIC_PALETTES[i % TOPIC_PALETTES.length]]));

const TAG_CLASS = {
  'physical-reservoir-computing':'tag-prc','reservoir-computing':'tag-rc',
  'dynamical-systems':'tag-dyn','nonlinear-dynamics':'tag-dyn',
  'embodied-intelligence':'tag-emb','mechanical-intelligence':'tag-emb',
  'morphological-computation':'tag-emb','soft-robotics':'tag-emb',
  'soft-body-dynamics':'tag-emb','robot-learning':'tag-emb',
  'memory-capacity':'tag-mem','neuromorphic-computing':'tag-neuro',
};
const TYPE_ICON  = {theory:'⚗',experiment:'🔬',simulation:'💻',review:'📖'};
const TYPE_COLOR = {theory:'#c0607a',experiment:'#E5751F',simulation:'#4A7FB5',review:'#2E7D78'};

// ── Stats / topic bar ─────────────────────────────────────────
let activeTopicFilter = '', activeTypeFilter = '';

function buildStats(){
  document.getElementById('total-count').textContent = PAPERS.length;
  const bar = document.getElementById('stats-bar');

  // Topic chips
  bar.innerHTML += `<span class="bar-label">Topic</span>`;
  ALL_TOPICS.forEach(topic => {
    const count = PAPERS.filter(p=>p.topic===topic).length;
    const pal   = TOPIC_PAL[topic];
    const id    = 'tchip-'+topic.replace(/\s+/g,'_');
    bar.innerHTML += `<span class="stat-chip" id="${id}" onclick="toggleTopicChip('${topic}')"
      style="--chip-bg:rgba(255,255,255,.1);">
      <span class="dot" style="background:${pal.dot}"></span>${topic}: ${count}
    </span>`;
  });

  bar.innerHTML += `<span class="bar-divider"></span><span class="bar-label">Type</span>`;
  ['theory','experiment','simulation','review'].forEach(t=>{
    const count = PAPERS.filter(p=>p.paper_type===t).length;
    if(!count) return;
    bar.innerHTML += `<span class="stat-chip" id="chip-${t}" onclick="toggleTypeChip('${t}')">
      <span class="dot" style="background:${TYPE_COLOR[t]}"></span>
      ${t.charAt(0).toUpperCase()+t.slice(1)}: ${count}
    </span>`;
  });
}

function toggleTopicChip(topic){
  activeTopicFilter = activeTopicFilter===topic ? '' : topic;
  document.querySelectorAll('[id^="tchip-"]').forEach(c=>c.classList.remove('active-filter'));
  if(activeTopicFilter){
    document.getElementById('tchip-'+activeTopicFilter.replace(/\s+/g,'_'))?.classList.add('active-filter');
  }
  applyFilters();
}
function toggleTypeChip(type){
  activeTypeFilter = activeTypeFilter===type ? '' : type;
  document.querySelectorAll('[id^="chip-"]').forEach(c=>c.classList.remove('active-filter'));
  if(activeTypeFilter) document.getElementById('chip-'+activeTypeFilter)?.classList.add('active-filter');
  applyFilters();
}

// ── Year filter ───────────────────────────────────────────────
function buildYearFilter(){
  const years=[...new Set(PAPERS.map(p=>p.year).filter(Boolean))].sort((a,b)=>b-a);
  const sel=document.getElementById('year-filter');
  years.forEach(y=>{ const o=document.createElement('option');o.value=y;o.textContent=y;sel.appendChild(o); });
}

// ── Tag filter chips ──────────────────────────────────────────
const ALL_TAGS=[...new Set(PAPERS.flatMap(p=>p.tags))].sort();
let activeTags=new Set();
function buildTagFilters(){
  const c=document.getElementById('tag-filters');
  ALL_TAGS.forEach(tag=>{
    const b=document.createElement('span');
    b.className='filter-tag';b.textContent=tag;b.dataset.tag=tag;
    b.onclick=()=>toggleTag(tag,b);c.appendChild(b);
  });
}
function toggleTag(tag,btn){
  if(activeTags.has(tag)){activeTags.delete(tag);btn.classList.remove('active');}
  else{activeTags.add(tag);btn.classList.add('active');}
  applyFilters();
}

// ── Row renderer ──────────────────────────────────────────────
function makeTagHtml(tags){
  return tags.map(t=>`<span class="tag ${TAG_CLASS[t]||'tag-other'}" onclick="filterByTag(event,'${t}')">${t}</span>`).join('');
}
function topicBadgeHtml(topic){
  const pal=TOPIC_PAL[topic]||TOPIC_PALETTES[0];
  return `<span class="topic-badge"
    style="background:${pal.bg};color:${pal.color};border:1px solid ${pal.border};"
    onclick="filterByTopic(event,'${topic}')">${topic}</span>`;
}
function renderRow(p,idx){
  const tc='type-'+(p.paper_type||'other');
  const sc='status-'+(p.read_status||'unread').toLowerCase();
  return `
<tr class="paper-row" data-idx="${idx}" onclick="toggleDetail(${idx},this)">
  <td style="text-align:center;"><span class="expand-btn">+</span></td>
  <td><span class="cite-key">${p.citation_key}</span></td>
  <td><div class="paper-title">${p.title}</div></td>
  <td>${p.authors}</td>
  <td><span class="year-badge">${p.year}</span></td>
  <td>${topicBadgeHtml(p.topic)}</td>
  <td><span class="type-badge ${tc}">${TYPE_ICON[p.paper_type]||'•'} ${p.paper_type}</span></td>
  <td><span class="status-badge ${sc}">${p.read_status}</span></td>
  <td><div class="tags-cell">${makeTagHtml(p.tags)}</div></td>
</tr>
<tr class="detail-row" id="detail-${idx}" style="display:none;">
  <td colspan="9"><div class="detail-inner">${p.body_html}</div></td>
</tr>`;
}

// ── Sort ──────────────────────────────────────────────────────
let sortCol=4, sortDir=-1;
const COL_KEY={
  1:p=>p.citation_key, 2:p=>p.title, 3:p=>p.authors,
  4:p=>parseInt(p.year)||0, 5:p=>p.topic,
  6:p=>p.paper_type, 7:p=>p.read_status,
};
function sortBy(col){
  sortDir = sortCol===col ? -sortDir : (col===4?-1:1);
  sortCol=col;
  document.querySelectorAll('thead th').forEach((th,i)=>{
    th.classList.remove('sorted-asc','sorted-desc');
    if(i===col) th.classList.add(sortDir===1?'sorted-asc':'sorted-desc');
  });
  applyFilters();
}

// ── Filter + render ───────────────────────────────────────────
function applyFilters(){
  const q=document.getElementById('search').value.toLowerCase().trim();
  const status=document.getElementById('status-filter').value;
  const year=document.getElementById('year-filter').value;

  let filtered=PAPERS.filter(p=>{
    if(q && !`${p.title} ${p.authors} ${p.citation_key}`.toLowerCase().includes(q)) return false;
    if(activeTopicFilter && p.topic!==activeTopicFilter) return false;
    if(activeTypeFilter  && p.paper_type!==activeTypeFilter)  return false;
    if(status && p.read_status!==status) return false;
    if(year   && String(p.year)!==year)  return false;
    if(activeTags.size && ![...activeTags].every(t=>p.tags.includes(t))) return false;
    return true;
  });

  const kf=COL_KEY[sortCol];
  if(kf) filtered.sort((a,b)=>{const av=kf(a),bv=kf(b);return av<bv?-sortDir:av>bv?sortDir:0;});

  document.getElementById('tbody').innerHTML=filtered.map(p=>renderRow(p,PAPERS.indexOf(p))).join('');
  document.getElementById('results-count').textContent=
    filtered.length===PAPERS.length?`${PAPERS.length} papers`:`${filtered.length} / ${PAPERS.length}`;
  document.getElementById('no-results').style.display=filtered.length?'none':'block';
  document.getElementById('papers-table').style.display=filtered.length?'':'none';
}

// ── Detail expand ─────────────────────────────────────────────
function toggleDetail(idx,row){
  const d=document.getElementById('detail-'+idx);
  const open=d.style.display!=='none';
  d.style.display=open?'none':'table-row';
  row.classList.toggle('expanded',!open);
}

// ── Click-through filters ─────────────────────────────────────
function filterByTag(evt,tag){
  evt.stopPropagation();
  activeTags.clear();activeTags.add(tag);
  document.querySelectorAll('.filter-tag').forEach(b=>b.classList.toggle('active',b.dataset.tag===tag));
  applyFilters();
}
function filterByTopic(evt,topic){
  evt.stopPropagation();
  activeTopicFilter = activeTopicFilter===topic ? '' : topic;
  document.querySelectorAll('[id^="tchip-"]').forEach(c=>c.classList.remove('active-filter'));
  if(activeTopicFilter)
    document.getElementById('tchip-'+activeTopicFilter.replace(/\s+/g,'_'))?.classList.add('active-filter');
  applyFilters();
}

// ── Reset ─────────────────────────────────────────────────────
function resetFilters(){
  document.getElementById('search').value='';
  document.getElementById('status-filter').value='';
  document.getElementById('year-filter').value='';
  activeTags.clear();activeTopicFilter='';activeTypeFilter='';
  document.querySelectorAll('.filter-tag').forEach(b=>b.classList.remove('active'));
  document.querySelectorAll('.stat-chip').forEach(c=>c.classList.remove('active-filter'));
  sortCol=4;sortDir=-1;
  document.querySelectorAll('thead th').forEach((th,i)=>{
    th.classList.remove('sorted-asc','sorted-desc');
    if(i===4) th.classList.add('sorted-desc');
  });
  applyFilters();
}

buildStats();buildYearFilter();buildTagFilters();resetFilters();
document.querySelectorAll('thead th')[4]?.classList.add('sorted-desc');
</script>
</body>
</html>
"""


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    papers = collect_all()
    if not papers:
        print("No markdown files found under Research_Topics/")
        return

    for p in papers:
        p["body_html"] = md_to_html(p.get("body", ""))
        p.pop("body", None)
        p.pop("created", None)

    papers_json = json.dumps(papers, ensure_ascii=False)
    html = HTML.replace("__PAPERS_JSON__", papers_json)

    OUT_FILE.write_text(html, encoding="utf-8")
    print(f"Generated : {OUT_FILE}")
    print(f"Papers    : {len(papers)}")
    topics = sorted({p['topic'] for p in papers})
    for t in topics:
        n = sum(1 for p in papers if p['topic'] == t)
        print(f"  {t}: {n}")
    webbrowser.open(OUT_FILE.as_uri())


if __name__ == "__main__":
    main()
