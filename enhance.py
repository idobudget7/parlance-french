from pathlib import Path
p=Path(__file__).parent
f=p/'app.js'; s=f.read_text()
s=s.replace("const lessons=RAW.map", "const EXTRA=EXTENDED.map(r=>[r[1],r[0]+' · Guided progression',r[2],r[3],r[4],r[5]]);\nconst lessons=[...RAW,...EXTRA].map")
s=s.replace("const KEY='parlance-local-v1'", "const KEY='parlance-local-v1'")
s=s.replace("visit:saved.visit||''", "visit:saved.visit||'',placement:saved.placement||null,placementAnswers:[],listen:{},listeningMode:'audio',practiceText:saved.practiceText||{}")
s=s.replace("visit:state.visit}))", "visit:state.visit,placement:state.placement,practiceText:state.practiceText}))")
s=s.replace("else if(state.page==='practice')practice();else settings()", "else if(state.page==='practice')practice();else if(state.page==='placement')placement();else if(state.page==='listening')listening();else settings()")
s=s.replace("${nav('practice','Practice','✎')}","${nav('practice','Practice','✎')}${nav('listening','Listening','♫')}${nav('placement','Placement','◎')}")
s=s.replace("Designed for practical beginner French. CEFR-inspired sequence, not an official proficiency assessment.", "A1–B2 learning pathway, not a comprehensive accredited course or official proficiency assessment.")
s=s.replace("<b>A0 → A2</b>","<b>A0 → B2</b>")
s=s.replace("['all','A0','A1','A2']","['all','A0','A1','A2','B1','B2']")
s=s.replace("<button class=\"btn ghost\" aria-label=\"Hear ${escapeHTML(w.fr)}\" onclick=\"say(${JSON.stringify(w.fr).replace(/\"/g,'&quot;')})\">♫</button>","${audioButtons(w.fr)}")
s=s.replace("<button class=\"btn ghost\" onclick=\"say(${JSON.stringify(w.fr).replace(/\"/g,'&quot;')})\">♫ Hear</button>","${audioButtons(w.fr)}")
s=s.replace("<button class=\"btn ghost\" onclick=\"say(${JSON.stringify(line).replace(/\"/g,'&quot;')})\">♫ Listen</button>","${audioButtons(line)}")
s=s.replace("<button class=\"btn ghost\" style=\"padding:6px 10px;margin-top:7px\" onclick=\"say(${JSON.stringify(line).replace(/\"/g,'&quot;')})\">♫ Listen</button>","${audioButtons(line)}")
s=s.replace("${w.hint?' · Reading aid: '+escapeHTML(w.hint):''}"," · IPA: ${escapeHTML(ipaFor(w.fr))}${w.hint?' · Approx.: '+escapeHTML(w.hint):''}")
s=s.replace("${escapeHTML(w.hint||'What does this mean?')}","${escapeHTML(ipaFor(w.fr))}")
s=s.replace("<span class=\"eyebrow\">OPEN PRACTICE</span>","<span class=\"eyebrow\">OPEN PRACTICE</span>")
s=s.replace("<textarea id=\"practice${i}\" class=\"field\" rows=\"3\" placeholder=\"Type your own French response here…\"></textarea>","<textarea id=\"practice${i}\" class=\"field\" rows=\"3\" placeholder=\"Type your own French response here…\" oninput=\"savePractice(${i},this.value)\">${escapeHTML(state.practiceText[i]||'')}</textarea>")
s=s.replace("Practice responses are not stored.","Practice responses are saved only on this device.")
s=s.replace("Short phrase sets → multiple-choice recall → typed recall → dialogue practice → spaced review. CEFR-inspired foundations A0–A2, but not an official CEFR test or a complete A2 certification program.","A0 foundations, A1–B2 guided modules, reading, writing, contextual dialogue, linked pronunciation, optional listening tasks and spaced review. This is not a complete CEFR certification program; independent speaking/writing assessment and authentic recorded listening remain essential.")
s=s.replace("visit:state.visit};const a", "visit:state.visit,placement:state.placement,practiceText:state.practiceText};const a")
s=s.replace("state.minutes=p.minutes||0;save();", "state.minutes=p.minutes||0;state.placement=p.placement||null;state.practiceText=p.practiceText||{};save();")
s=s.replace("state.attempts={};save();", "state.attempts={};state.placement=null;state.practiceText={};save();")
s=s.replace("const options=['all'", "const options=['all'")
s=s.replace("${lessonRow(next)}<div class=\"sectionhead\">", "${lessonRow(next)}<div class=\"flex\" style=\"margin-top:13px\"><button class=\"btn secondary\" onclick=\"go('placement')\">Take adaptive placement check</button><button class=\"btn ghost\" onclick=\"go('listening')\">Listening practice</button></div><div class=\"sectionhead\">")
s=s.replace("French pronunciation cannot be mastered from written hints alone.","Google Translate pronunciation opens externally; click its speaker there. Sound is required for genuine listening assessments.")
s=s.replace("${q.w.hint?' Reading aid: '+escapeHTML(q.w.hint):''}"," · IPA: ${escapeHTML(ipaFor(q.w.fr))}")
s=s.replace("<div class=\"phonetic\">${escapeHTML(ipaFor(w.fr))}</div>","<div class=\"phonetic\">${escapeHTML(ipaFor(w.fr))}</div><div>${audioButtons(w.fr)}</div>")
s=s.replace("<p class=\"muted\">Uses your device's installed French speech voices, not downloaded MP3 files.","<p class=\"muted\">Optional on-device voices plus Google Translate pronunciation links (external, online; use the speaker button there). No MP3s are bundled.")
s=s.replace("'CEFR-inspired foundations A0–A2'", "'CEFR-inspired pathway A0–B2'")
# make IPA fallback unambiguous: no fabricated transcription
s += r'''
// IPA data is curated only for exact words. An unverified IPA transcription is never fabricated.
const IPA={
'Bonjour':'/bɔ̃.ʒuʁ/','Salut':'/sa.ly/','Bonsoir':'/bɔ̃.swaʁ/','Au revoir':'/o ʁə.vwaʁ/','Merci':'/mɛʁ.si/','S’il vous plaît':'/sil vu plɛ/','Oui':'/wi/','Non':'/nɔ̃/','Je suis…':'/ʒə sɥi/','Je m’appelle…':'/ʒə ma.pɛl/','Enchanté(e)':'/ɑ̃.ʃɑ̃.te/','Ça va ?':'/sa va/','Très bien.':'/tʁɛ bjɛ̃/','Pas mal.':'/pa mal/','Je vais bien.':'/ʒə vɛ bjɛ̃/','zéro':'/ze.ʁo/','un':'/œ̃/','deux':'/dø/','trois':'/tʁwa/','quatre':'/katʁ/','cinq':'/sɛ̃k/','six':'/sis/','sept':'/sɛt/','huit':'/ɥit/','neuf':'/nœf/','dix':'/dis/','la famille':'/la fa.mij/','la mère':'/la mɛʁ/','le père':'/lə pɛʁ/','les parents':'/le pa.ʁɑ̃/','un enfant':'/œ̃.nɑ̃.fɑ̃/','un frère':'/œ̃ fʁɛʁ/','une sœur':'/yn sœʁ/','de l’eau':'/də lo/','un café':'/œ̃ ka.fe/','un thé':'/œ̃ te/','du pain':'/dy pɛ̃/','du fromage':'/dy fʁɔ.maʒ/','une pomme':'/yn pɔm/','aujourd’hui':'/o.ʒuʁ.dɥi/','demain':'/də.mɛ̃/','hier':'/jɛʁ/','lundi':'/lœ̃.di/','mardi':'/maʁ.di/','mercredi':'/mɛʁ.kʁə.di/','jeudi':'/ʒø.di/','vendredi':'/vɑ̃.dʁə.di/','samedi':'/sam.di/','dimanche':'/di.mɑ̃ʃ/','à gauche':'/a ɡoʃ/','à droite':'/a dʁwat/','tout droit':'/tu dʁwa/','ici':'/i.si/','là-bas':'/la.ba/','parce que':'/paʁs kə/','mais':'/mɛ/','donc':'/dɔ̃k/','Je ne comprends pas.':'/ʒə nə kɔ̃.pʁɑ̃ pa/','je pense que…':'/ʒə pɑ̃s kə/','je préfère…':'/ʒə pʁe.fɛʁ/','j’ai':'/ʒe/','je suis':'/ʒə sɥi/','nous sommes':'/nu sɔm/','nous avons':'/nu.za.vɔ̃/'};
function ipaFor(v){return IPA[v]||'IPA not yet verified — open Google pronunciation';}
function googleURL(t){return 'https://translate.google.com/?sl=fr&tl=en&text='+encodeURIComponent(t)+'&op=translate'}
function audioButtons(t){const x=escapeHTML(t);return `<span class="flex" style="gap:5px"><a class="btn ghost" style="text-decoration:none;padding:8px 10px" href="${escapeHTML(googleURL(t))}" target="_blank" rel="noopener noreferrer" aria-label="Open Google pronunciation for ${x}">↗ Google pronunciation</a><button class="btn ghost" style="padding:8px 10px" onclick="say(${JSON.stringify(t).replace(/"/g,'&quot;')})" aria-label="Play optional device voice for ${x}">♫ Device</button></span>`}
function savePractice(i,v){state.practiceText[i]=v;save()}
const LEVELS=['A1','A2','B1','B2'];
const PLACEMENT=[
 ['A1','What does « Je voudrais un café » mean?',['I would like a coffee','I own a café','The café is closed'],0],
 ['A1','Choose the correct French: “I am 30 years old.”',['Je suis trente ans.','J’ai trente ans.','Je fais trente ans.'],1],
 ['A1','Which is the polite way to ask “where is the station”?',['Où est la gare, s’il vous plaît ?','Où gare vous ?','Tu gare où ?'],0],
 ['A2','“Je suis allé au marché hier.” The action took place…',['Tomorrow','Yesterday','Every day'],1],
 ['A2','Choose the appropriate future plan.',['Je vais partir demain.','Je partir hier.','Je suis partir demain.'],0],
 ['A2','« Il travaille depuis deux ans. » means…',['He stopped two years ago.','He has been working for two years.','He will start in two years.'],1],
 ['B1','Choose a logical consequence: « Il pleuvait, ___ nous sommes restés chez nous. »',['pourtant','donc','malgré'],1],
 ['B1','« Si j’avais plus de temps, je voyagerais. » describes…',['An unreal present condition','A completed past event','A command'],0],
 ['B1','Which response politely disagrees?',['Tu as toujours tort.','Je comprends votre avis, mais je ne suis pas d’accord.','N’importe quoi !'],1],
 ['B2','« Bien qu’il soit tard » uses the…',['conditional','subjunctive','future'],1],
 ['B2','« Si nous avions su, nous aurions agi. » refers to…',['An unreal past outcome','A routine','An ongoing action'],0],
 ['B2','Which most carefully qualifies a conclusion?',['C’est absolument certain.','Cela semble plausible, mais les données restent limitées.','Tout le monde le sait.'],1]
];
let placementRun={index:0,history:[],done:false};
function placement(){const z=placementRun;if(z.done){const correct=z.history.filter(a=>a.correct).length;const by=LEVELS.map(k=>{let qs=PLACEMENT.filter(x=>x[0]===k);return [k,qs.filter(x=>z.history.some(h=>h.i===PLACEMENT.indexOf(x)&&h.correct)).length,qs.length]});const highest=by.reduce((acc,[k,n,total])=>n>=2?k:acc,'A1');state.placement={score:correct,total:PLACEMENT.length,suggested:highest,by,at:Date.now()};save();frame(`<div class="study"><h1>Placement estimate: ${highest}</h1><p>${correct}/${PLACEMENT.length} correct. This is a short, non-standardized knowledge screen, <b>not a certified CEFR placement</b>. It does not test unscripted speech or authentic listening.</p><div class="card">${by.map(([k,n,t])=>`<p><b>${k}</b> · ${n} / ${t} correct</p>`).join('')}</div><div class="flex" style="margin-top:16px"><button class="btn" onclick="startAt('${highest}')">Explore ${highest} lessons</button><button class="btn secondary" onclick="restartPlacement()">Retake check</button></div></div>`);return}
const i=z.index;const item=PLACEMENT[i];frame(`<div class="study"><div class="eyebrow">ADAPTIVE ENTRY CHECK · ${i+1}/${PLACEMENT.length}</div><h1>${escapeHTML(item[1])}</h1><p class="muted">Level band: ${item[0]}. Questions are presented in sequence; a wrong answer skips the remaining questions in that band to avoid frustration.</p><div class="options">${item[2].map((x,j)=>`<button class="choice" onclick="placeAnswer(${j})">${escapeHTML(x)}</button>`).join('')}</div><button class="btn ghost" style="margin-top:15px" onclick="restartPlacement()">Restart</button></div>`)}
function placeAnswer(v){const z=placementRun;const i=z.index;const right=PLACEMENT[i][3]===v;z.history.push({i,correct:right});z.index=right?i+1:Math.min(PLACEMENT.length,(Math.floor(i/3)+1)*3);if(z.index>=PLACEMENT.length)z.done=true;placement()}
function restartPlacement(){placementRun={index:0,history:[],done:false};placement()}
function startAt(k){state.filter=k;showPage('course')}
// Listening assessment: only audio-first when speech synthesis is available; Google option requires user-controlled external playback.
const LISTEN=[
{level:'A1',fr:'Bonjour, je voudrais un café, s’il vous plaît.',q:'What is the customer ordering?',options:['A coffee','A train ticket','A room'],a:0},
{level:'A1',fr:'Le rendez-vous est mardi à quinze heures.',q:'When is the appointment?',options:['Monday at 5','Tuesday at 3','Thursday at 10'],a:1},
{level:'A2',fr:'Mon train est en retard, je vais arriver après dix heures.',q:'What is the main problem?',options:['The train is late','The train is cancelled','The train is full'],a:0},
{level:'A2',fr:'Je suis allé au marché hier, puis j’ai préparé le dîner.',q:'What happened after the market?',options:['A meeting','Prepared dinner','Went to work'],a:1},
{level:'B1',fr:'Même si le prix est plus élevé, je préfère cette option parce qu’elle est plus fiable.',q:'Why is the more expensive option preferred?',options:['It is faster','It is more reliable','It is nearby'],a:1},
{level:'B1',fr:'Si j’avais plus de temps, je participerais à la formation prévue pour la semaine prochaine.',q:'What prevents the speaker from joining?',options:['Lack of time','No interest','Price'],a:0},
{level:'B2',fr:'Bien que les résultats soient encourageants, il serait prématuré d’affirmer que la méthode est définitivement efficace.',q:'How does the speaker view the findings?',options:['Definitive proof','Promising but inconclusive','Completely negative'],a:1},
{level:'B2',fr:'Les intervenants s’accordent sur le diagnostic, mais divergent quant aux mesures à mettre en œuvre.',q:'What do the speakers disagree about?',options:['The diagnosis','The proposed actions','Whether a problem exists'],a:1}
];
let listenRun={i:0,answers:[],revealed:false,completed:false};
function listening(){let z=listenRun, l=LISTEN[z.i];if(z.completed){const n=z.answers.filter(Boolean).length;frame(`<div class="study"><h1>${state.listeningMode==='audio'?'Listening':'Reading'} check complete</h1><p>${n}/${LISTEN.length} correct · ${state.listeningMode==='audio'?'Audio attempted':'Text-first comprehension; not listening proficiency'}</p><button class="btn" onclick="restartListening()">Try again</button><button class="btn secondary" onclick="go('course')">Continue lessons</button></div>`);return}
frame(`<div class="study"><div class="eyebrow">${state.listeningMode==='audio'?'AUDIO-FIRST COMPREHENSION':'READING COMPREHENSION'} · ${z.i+1}/${LISTEN.length} · ${l.level}</div><h1>Understand the message.</h1><p class="muted">Use the external Google speaker to hear the French, then return here. Google does not autoplay from this site. A text-only option is available, but cannot count as a listening assessment.</p><div class="flex" style="margin:14px 0"><button class="btn ${state.listeningMode==='audio'?'':'secondary'}" onclick="switchListening('audio')">Audio-first</button><button class="btn ${state.listeningMode==='reading'?'':'secondary'}" onclick="switchListening('reading')">Reading fallback</button></div><div class="card"><div class="flex">${audioButtons(l.fr)}</div>${state.listeningMode==='reading'||z.revealed?`<p lang="fr" style="font-size:20px">${escapeHTML(l.fr)}</p>`:`<p class="muted">The sentence is hidden for a genuine audio-first attempt. Use Google pronunciation or your device voice before answering.</p>`}${state.listeningMode==='audio'?`<button class="btn ghost" onclick="revealListening()">Reveal transcript (converts this question to reading)</button>`:''}</div><div class="question">${escapeHTML(l.q)}</div><div class="options">${l.options.map((x,j)=>`<button class="choice" onclick="listenAnswer(${j})">${escapeHTML(x)}</button>`).join('')}</div></div>`)}
function switchListening(v){state.listeningMode=v;listenRun.revealed=false;listening()}
function revealListening(){listenRun.revealed=true;listening()}
function listenAnswer(v){const z=listenRun,l=LISTEN[z.i];z.answers.push(v===l.a);const good=v===l.a;const assessed=state.listeningMode==='audio'&&!z.revealed;z.i++;if(z.i>=LISTEN.length)z.completed=true;listening();notice(`${good?'Correct':'Review this one'}. ${assessed?'Marked audio-first (self-reported listening).':'Marked as text-supported.'}`)}
function restartListening(){listenRun={i:0,answers:[],revealed:false,completed:false};listening()}
'''
f.write_text(s)
h=p/'index.html';t=h.read_text().replace('<script src="app.js"></script>','<script src="advanced.js"></script><script src="app.js"></script>');h.write_text(t)
