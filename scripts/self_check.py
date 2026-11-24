"""Generate the student self-check page (self-check/index.html) in the XA design system.

The page is a single static HTML file. Students pick one answer per question; answers and
explanations stay hidden until they press "Check answers". Nothing is recorded or sent anywhere.
"""
import datetime
import html
import re
from html.parser import HTMLParser

from formatting import to_html

FONT_DIR = '../assets/fonts'

CSS = """
@font-face{font-family:"PT Sans";font-weight:400;font-style:normal;font-display:swap;
 src:local("PT Sans"),local("PTSans-Regular"),url("%(fonts)s/ptsans/PT_Sans-Web-Regular.ttf") format("truetype")}
@font-face{font-family:"PT Sans";font-weight:700;font-style:normal;font-display:swap;
 src:local("PT Sans Bold"),local("PTSans-Bold"),url("%(fonts)s/ptsans/PT_Sans-Web-Bold.ttf") format("truetype")}
@font-face{font-family:"JetBrains Mono";font-weight:100 800;font-style:normal;font-display:swap;
 src:local("JetBrains Mono"),url("%(fonts)s/jetbrainsmono/JetBrainsMono[wght].ttf") format("truetype")}
:root{--xa-color-rose:#d27079;--xa-color-rose-hover:#c15f69;--xa-color-navy:#3d496e;--xa-color-slate:#535c73;
--xa-color-maroon:#800000;--xa-color-green:#16a34a;--xa-color-green-ink:#11803a;--xa-color-sky:#0ea5e9;--xa-color-white:#fff;
--xa-color-canvas:#f5f5f7;--xa-color-line:#e9e9ef;--xa-color-muted:#8991a8;--xa-color-ink:#212121;
--xa-color-rose-soft:#f7e6e8;--xa-color-slate-soft:#eceef3;--xa-color-green-soft:#e7f5ec;--xa-color-maroon-soft:#f6e6e6;
--xa-color-amber:#d97706;--xa-color-amber-soft:#fdf0db;
--xa-font-sans:"PT Sans",system-ui,-apple-system,"Segoe UI",sans-serif;--xa-font-mono:"JetBrains Mono",ui-monospace,monospace;
--xa-radius-sm:6px;--xa-radius-md:9px;--xa-radius-lg:14px;
--xa-shadow-sm:0 1px 2px rgba(33,33,33,.06),0 1px 1px rgba(33,33,33,.04);
--xa-shadow-md:0 6px 18px rgba(61,73,110,.12),0 2px 5px rgba(33,33,33,.05);
--xa-ring:0 0 0 3px rgba(210,112,121,.28);color-scheme:light}
*,*:before,*:after{box-sizing:border-box;margin:0;padding:0}
html{scroll-padding-top:150px}
body{font-family:var(--xa-font-sans);color:var(--xa-color-ink);background:var(--xa-color-canvas);line-height:1.55;
 -webkit-font-smoothing:antialiased;font-size:16px}
h1,h2,h3{line-height:1.2;color:var(--xa-color-navy);font-weight:700}
code{font-family:var(--xa-font-mono);font-size:.82em;background:var(--xa-color-line);padding:2px 6px;border-radius:5px;color:var(--xa-color-navy)}
.wrap{max-width:920px;margin:0 auto;padding:0 28px}
.xa-header{position:sticky;top:0;z-index:100;background:#ffffffe0;backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);
 border-bottom:1px solid var(--xa-color-line)}
.xa-header-row{display:flex;align-items:center;gap:20px;height:64px}
.xa-header-brand{display:flex;align-items:center;flex-shrink:0}
.xa-header-brand svg{height:26px;width:auto;display:block}
.xa-header-title{color:var(--xa-color-navy);font-weight:700;font-size:.94rem;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.xa-header-spacer{flex:1}
.ver-badge{font-family:var(--xa-font-mono);font-size:.78rem;color:var(--xa-color-muted);border:1px solid var(--xa-color-line);
 border-radius:999px;padding:4px 11px;white-space:nowrap}
.c-hero{padding:44px 0 22px}
.eyebrow{color:var(--xa-color-rose);font-weight:700;letter-spacing:.04em;text-transform:uppercase;font-size:.78rem}
.c-hero h1{font-size:2.6rem;margin:8px 0 10px;letter-spacing:-.02em}
.c-hero h1 .hl{background:linear-gradient(transparent 60%%,var(--xa-color-rose-soft) 60%%);padding:0 3px}
.c-hero p.lead{font-size:1.1rem;color:var(--xa-color-muted);max-width:720px}
.tabs-bar{position:sticky;top:64px;z-index:90;background:var(--xa-color-canvas)}
.xa-tabs-list{display:flex;gap:4px;border-bottom:1px solid var(--xa-color-line);overflow-x:auto;scrollbar-width:thin}
.xa-tabs-tab{appearance:none;background:none;border:none;cursor:pointer;font-family:inherit;font-weight:700;font-size:.92rem;
 color:var(--xa-color-slate);padding:11px 14px;margin-bottom:-1px;border-bottom:2px solid transparent;transition:color .12s;white-space:nowrap}
.xa-tabs-tab:hover{color:var(--xa-color-navy)}
.xa-tabs-tab:focus-visible{outline:none;box-shadow:var(--xa-ring);border-radius:6px}
.xa-tabs-tab[aria-selected=true]{color:var(--xa-color-rose);border-bottom-color:var(--xa-color-rose)}
.xa-tabs-panel{padding:26px 0 8px}
.xa-tabs-panel[hidden]{display:none}
.panel-head{margin-bottom:18px}
.panel-head h2{font-size:1.6rem;letter-spacing:-.01em;margin:6px 0 10px}
.badges{display:flex;gap:6px;flex-wrap:wrap}
.badge{display:inline-flex;align-items:center;gap:5px;font-size:.76rem;font-weight:700;padding:3px 9px;border-radius:999px;line-height:1.3;white-space:nowrap}
.b-neutral{background:var(--xa-color-slate-soft);color:var(--xa-color-slate)}
.b-feat{background:var(--xa-color-navy);color:#fff}
.b-ok{background:var(--xa-color-green-soft);color:var(--xa-color-green-ink)}
.b-err{background:var(--xa-color-maroon-soft);color:var(--xa-color-maroon)}
.card{background:var(--xa-color-white);border:1px solid var(--xa-color-line);border-radius:var(--xa-radius-lg);box-shadow:var(--xa-shadow-sm)}
.q{padding:20px 22px;margin:0 0 16px;min-width:0}
.q legend{float:left;width:100%%;display:flex;gap:12px;align-items:flex-start;padding:0;margin-bottom:10px}
.q legend+*{clear:both}
.num{display:inline-grid;place-items:center;flex-shrink:0;width:28px;height:28px;border-radius:50%%;background:var(--xa-color-rose-soft);
 color:var(--xa-color-rose);font-size:.82rem;font-weight:700;margin-top:-2px}
.q-title{flex:1;color:var(--xa-color-navy);font-weight:700;font-size:1.05rem;line-height:1.35}
.q .scenario{margin-left:6px;vertical-align:2px}
.prompt p{margin:0 0 12px;color:var(--xa-color-ink)}
.opts{display:grid;gap:8px}
.opt{display:grid;grid-template-columns:18px 22px minmax(0,1fr);gap:10px;align-items:start;border:1px solid var(--xa-color-line);
 border-radius:var(--xa-radius-md);padding:10px 14px;cursor:pointer;background:var(--xa-color-white);transition:border-color .12s,background .12s}
.opt:hover{border-color:#cdd2dd;background:var(--xa-color-canvas)}
.opt input{margin:5px 0 0;accent-color:var(--xa-color-rose);width:16px;height:16px}
.opt input:focus-visible{outline:none;box-shadow:var(--xa-ring);border-radius:50%%}
.opt .lbl{font-weight:700;color:var(--xa-color-navy)}
.opt:has(input:checked){border-color:var(--xa-color-rose);box-shadow:var(--xa-ring);background:var(--xa-color-white)}
.done .opt{cursor:default}
.done .opt:hover{border-color:var(--xa-color-line);background:var(--xa-color-white)}
.done .opt.is-correct{background:var(--xa-color-green-soft);border-color:var(--xa-color-green);box-shadow:none}
.done .opt.is-wrong{background:var(--xa-color-maroon-soft);border-color:var(--xa-color-maroon);box-shadow:none}
.opt .tag{display:none}
.done .opt.is-correct .tag,.done .opt.is-wrong .tag{display:inline-flex;margin-left:8px;vertical-align:1px}
.xa-alert{display:flex;align-items:flex-start;gap:11px;border:1px solid transparent;border-left-width:4px;border-radius:var(--xa-radius-md);
 padding:13px 15px;font-size:.94rem;line-height:1.5;margin-top:14px}
.xa-alert[hidden]{display:none}
.xa-alert-icon{flex-shrink:0;display:block;width:20px;height:20px;line-height:20px;text-align:center;font-weight:700}
.xa-alert-content{flex:1;min-width:0}
.xa-alert-title{font-weight:700;margin:0 0 2px}
.xa-alert-body{color:var(--xa-color-navy)}
.xa-alert-body p{margin:0 0 6px}.xa-alert-body p:last-child{margin:0}
.xa-alert-ok{background:var(--xa-color-green-soft);border-color:var(--xa-color-green)}
.xa-alert-ok .xa-alert-title,.xa-alert-ok .xa-alert-icon{color:var(--xa-color-green-ink)}
.xa-alert-err{background:var(--xa-color-maroon-soft);border-color:var(--xa-color-maroon)}
.xa-alert-err .xa-alert-title,.xa-alert-err .xa-alert-icon{color:var(--xa-color-maroon)}
.xa-alert-warning{background:var(--xa-color-amber-soft);border-color:var(--xa-color-amber)}
.xa-alert-warning .xa-alert-title,.xa-alert-warning .xa-alert-icon{color:#9a6a00}
.missing{border-color:var(--xa-color-amber);box-shadow:0 0 0 3px rgba(217,119,6,.18)}
.actions{display:flex;flex-wrap:wrap;align-items:center;gap:12px;margin:22px 0 8px;padding:18px 20px}
.btn{font-family:var(--xa-font-sans);font-weight:700;font-size:.94rem;border:1px solid transparent;border-radius:var(--xa-radius-md);
 padding:10px 18px;cursor:pointer;display:inline-flex;align-items:center;gap:8px;transition:.15s;line-height:1}
.btn:focus-visible{outline:none;box-shadow:var(--xa-ring)}
.btn-primary{background:var(--xa-color-rose);color:#fff}.btn-primary:hover{background:var(--xa-color-rose-hover)}
.btn-primary:disabled{background:#e3b3b8;cursor:default}
.btn-secondary{background:var(--xa-color-white);color:var(--xa-color-navy);border-color:#cdd2dd}.btn-secondary:hover{border-color:var(--xa-color-navy)}
.score{display:flex;align-items:baseline;gap:10px;margin-left:auto;color:var(--xa-color-slate);font-size:.92rem}
.score strong{font-size:1.6rem;color:var(--xa-color-navy);letter-spacing:-.02em}
.score .pending{color:#9a6a00;font-weight:700}
footer a{color:inherit;text-decoration:underline}
footer{padding:28px 0 60px;color:var(--xa-color-muted);font-size:.85rem;text-align:center}
@media (max-width:640px){.wrap{padding:0 16px}.c-hero{padding:30px 0 16px}.c-hero h1{font-size:2rem}.xa-header-title{display:none}
 .q{padding:16px}.opt{padding:10px 12px;gap:8px}.score{margin-left:0;width:100%%}}
""" % {'fonts': FONT_DIR}

SCRIPT = """
(function () {
  var tabs = Array.prototype.slice.call(document.querySelectorAll('.xa-tabs-tab'));
  var panels = Array.prototype.slice.call(document.querySelectorAll('.xa-tabs-panel'));
  var KEY = 'ica0024-self-check-tab';
  function show(id, focus) {
    tabs.forEach(function (t) {
      var on = t.getAttribute('aria-controls') === id;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      if (on && focus) t.focus();
      if (on) { var list = t.parentNode; list.scrollLeft = t.offsetLeft - (list.clientWidth - t.clientWidth) / 2; }
    });
    panels.forEach(function (p) { p.hidden = p.id !== id; });
    try { localStorage.setItem(KEY, id); } catch (e) {}
  }
  tabs.forEach(function (t, i) {
    t.addEventListener('click', function () { show(t.getAttribute('aria-controls')); });
    t.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!d) return;
      e.preventDefault();
      show(tabs[(i + d + tabs.length) % tabs.length].getAttribute('aria-controls'), true);
    });
  });
  var first = panels[0].id;
  try { var saved = localStorage.getItem(KEY); if (saved && document.getElementById(saved)) first = saved; } catch (e) {}
  show(first);

  function shuffle(panel) {
    panel.querySelectorAll('.opts').forEach(function (box) {
      var opts = Array.prototype.slice.call(box.children);
      for (var i = opts.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1)); var t = opts[i]; opts[i] = opts[j]; opts[j] = t;
      }
      opts.forEach(function (o, i) { o.querySelector('.lbl').textContent = 'ABCD'[i] + '.'; box.appendChild(o); });
    });
  }

  panels.forEach(function (panel) {
    shuffle(panel);
    var check = panel.querySelector('.js-check'), reset = panel.querySelector('.js-reset'), score = panel.querySelector('.score');
    var questions = Array.prototype.slice.call(panel.querySelectorAll('.q'));
    check.addEventListener('click', function () {
      var open = questions.filter(function (q) { return !q.querySelector('input:checked'); });
      questions.forEach(function (q) { q.classList.toggle('missing', open.indexOf(q) >= 0); });
      if (open.length) {
        score.innerHTML = '<span class="pending">' + open.length + ' question' + (open.length > 1 ? 's' : '') +
          ' still unanswered.</span>';
        open[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
        return;
      }
      var got = 0, total = 0, right = 0;
      questions.forEach(function (q) {
        var pts = +q.getAttribute('data-points'), chosen = q.querySelector('input:checked').closest('.opt');
        var ok = chosen.getAttribute('data-key') === '1';
        total += pts; if (ok) { got += pts; right++; }
        q.classList.add('done');
        q.querySelectorAll('input').forEach(function (i) { i.disabled = true; });
        q.querySelectorAll('.opt').forEach(function (o) {
          if (o.getAttribute('data-key') === '1') o.classList.add('is-correct');
          else if (o === chosen) o.classList.add('is-wrong');
        });
        var fb = q.querySelector('.xa-alert');
        fb.classList.add(ok ? 'xa-alert-ok' : 'xa-alert-err');
        fb.querySelector('.xa-alert-icon').textContent = ok ? '\\u2713' : '\\u2715';
        fb.querySelector('.xa-alert-title').textContent = ok ? 'Correct' : 'Not quite';
        fb.hidden = false;
      });
      score.innerHTML = '<strong>' + got + ' / ' + total + '</strong><span>marks, ' + right + ' of ' +
        questions.length + ' correct</span>';
      check.disabled = true;
    });
    reset.addEventListener('click', function () {
      questions.forEach(function (q) {
        q.classList.remove('done', 'missing');
        q.querySelectorAll('.opt').forEach(function (o) { o.classList.remove('is-correct', 'is-wrong'); });
        var fb = q.querySelector('.xa-alert');
        fb.hidden = true; fb.classList.remove('xa-alert-ok', 'xa-alert-err');
      });
      panel.querySelectorAll('input').forEach(function (i) { i.checked = false; i.disabled = false; });
      check.disabled = false; score.innerHTML = ''; shuffle(panel);
      panel.scrollIntoView({ behavior: 'smooth' });
    });
  });
})();
"""


def _inline_html(markdown_text):
    """Render one line of Markdown and drop the wrapping paragraph."""
    rendered = to_html(markdown_text).strip()
    return re.sub(r'^<p>(.*)</p>$', r'\1', rendered, flags=re.S)


def _logo(svg_text):
    svg = re.sub(r'<\?xml[^>]*>\s*', '', svg_text).strip()
    return svg.replace('<svg ', '<svg role="img" aria-label="eXtreme Automation" ', 1)


def _question(q):
    qid = q['id'].replace(' ', '-')
    options = ''.join(
        f'<label class="opt" data-key="{1 if o["label"] == q["correct_option"] else 0}">'
        f'<input type="radio" name="{qid}" value="{o["label"]}">'
        f'<span class="lbl">{o["label"]}.</span>'
        f'<span class="txt">{_inline_html(o["text"])}'
        f'<span class="tag badge {"b-ok" if o["label"] == q["correct_option"] else "b-err"}">'
        f'{"Correct answer" if o["label"] == q["correct_option"] else "Your answer"}</span></span></label>'
        for o in q['options'])
    marks = f'{q["points"]} mark{"s" if q["points"] != 1 else ""}'
    scenario = '<span class="badge b-feat scenario">Scenario</span>' if q['number'] >= 9 else ''
    return (f'<fieldset class="card q" id="{qid}" data-points="{q["points"]}">'
            f'<legend><span class="num">{q["number"]}</span>'
            f'<span class="q-title">{html.escape(q["title"])}{scenario}</span>'
            f'<span class="badge b-neutral">{marks}</span></legend>'
            f'<div class="prompt">{to_html(q["prompt_markdown"])}</div>'
            f'<div class="opts">{options}</div>'
            f'<div class="xa-alert" role="status" hidden><span class="xa-alert-icon" aria-hidden="true"></span>'
            f'<div class="xa-alert-content"><p class="xa-alert-title"></p>'
            f'<div class="xa-alert-body">{to_html(q["grader_markdown"])}</div></div></div>'
            f'</fieldset>')


def render(questions, titles, logo_svg):
    lectures = sorted(titles)
    tabs, panels = [], []
    for lecture in lectures:
        group = [q for q in questions if q['lecture'] == lecture]
        total = sum(q['points'] for q in group)
        tabs.append(f'<button class="xa-tabs-tab" role="tab" id="tab-{lecture}" aria-controls="lecture-{lecture}" '
                    f'aria-selected="false" tabindex="-1">Lecture {lecture}</button>')
        panels.append(
            f'<section class="xa-tabs-panel" role="tabpanel" id="lecture-{lecture}" aria-labelledby="tab-{lecture}" '
            f'data-lecture="{lecture}" hidden>'
            f'<div class="panel-head"><p class="eyebrow">Lecture {lecture}</p><h2>{html.escape(titles[lecture])}</h2>'
            f'<div class="badges"><span class="badge b-neutral">{len(group)} questions</span>'
            f'<span class="badge b-neutral">{total} marks</span>'
            f'<span class="badge b-neutral">One correct answer each</span></div></div>'
            + ''.join(_question(q) for q in group) +
            f'<div class="card actions"><button type="button" class="btn btn-primary js-check">Check answers</button>'
            f'<button type="button" class="btn btn-secondary js-reset">Start again</button>'
            f'<div class="score" aria-live="polite"></div></div></section>')
    count = len(lectures)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="color-scheme" content="light">
<link rel="icon" href="data:,">
<title>ICA0024 Self-check</title>
<meta name="description" content="Self-check questionnaires for the ICA0024 Infrastructure as Code lectures. Answers stay hidden until checked.">
<style>{CSS}</style>
</head>
<body>
<header class="xa-header"><div class="wrap xa-header-row">
<a class="xa-header-brand" href="https://extremeautomation.io" rel="noopener" target="_blank" aria-label="eXtreme Automation">{_logo(logo_svg)}</a>
<span class="xa-header-title">ICA0024 Infrastructure as Code</span>
<span class="xa-header-spacer"></span>
<span class="ver-badge">self-check · {count} lectures</span>
</div></header>
<main class="wrap">
<section class="c-hero">
<p class="eyebrow">ICA0024 · Infrastructure as Code</p>
<h1>Lecture <span class="hl">self-check</span></h1>
<p class="lead">Ten questions per lecture to test your understanding. Pick one answer for each question, then check your answers to see your score and an explanation for every question. This is practice, not an exam: nothing is recorded or sent anywhere.</p>
</section>
<div class="tabs-bar"><nav class="xa-tabs-list" role="tablist" aria-label="Lectures">{''.join(tabs)}</nav></div>
{''.join(panels)}
</main>
<footer class="wrap">Generated from the ICA0024 questionnaire sources. Answer order is shuffled on each visit and after Start again.<br>© 2011-{datetime.date.today().year} Andrey Adamovich · <a href="https://extremeautomation.io" rel="noopener">extremeautomation.io</a></footer>
<script>{SCRIPT}</script>
</body>
</html>
"""


class _Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.questions = {}
        self.current = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'fieldset' and 'q' in attrs.get('class', '').split():
            self.current = attrs['id']
            self.questions[self.current] = {'points': int(attrs['data-points']), 'options': []}
        elif tag == 'label' and self.current and 'opt' in attrs.get('class', '').split():
            self.questions[self.current]['options'].append(attrs['data-key'])
        elif tag == 'input' and self.current and attrs.get('type') == 'radio':
            self.questions[self.current].setdefault('values', []).append(attrs['value'])


def validate(page, questions, titles):
    """Check that the page contains every question once with its four options and the right key."""
    collector = _Collector()
    collector.feed(page)
    found = collector.questions
    assert len(found) == len(questions), 'Self-check question count mismatch'
    for q in questions:
        item = found[q['id'].replace(' ', '-')]
        assert item['points'] == q['points']
        assert item['values'] == list('ABCD')
        assert item['options'] == ['1' if label == q['correct_option'] else '0' for label in 'ABCD']
    for lecture in titles:
        assert f'id="lecture-{lecture}"' in page and f'aria-controls="lecture-{lecture}"' in page
    assert '<script>' in page and 'Check answers' in page
    return {'questions': len(found), 'lectures': len(titles), 'bytes': len(page.encode())}


def build(questions, titles, logo_path, out_path):
    page = render(questions, titles, logo_path.read_text())
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(page)
    return out_path


if __name__ == '__main__':
    raise SystemExit('Run scripts/build.py, which generates self-check/index.html with the other exports.')
