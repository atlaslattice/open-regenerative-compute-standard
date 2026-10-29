// Standard-library DOM event harness. Not a browser rendering test.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const html=fs.readFileSync(process.argv[2],'utf8');
const starter=html.match(/<script id="starter" type="application\/json">([\s\S]*?)<\/script>/)[1];
const script=html.match(/<script>\n([\s\S]*?)<\/script>/)[1];
class Element{get value(){return this._value;}set value(x){this._value=String(x);}constructor(){this.value='';this.children=[];this.textContent='';}append(x){this.children.push(x);if(x.id)els[x.id]=x;}replaceChildren(){this.children=[];}setAttribute(k,v){this[k]=v;}click(){if(this.onclick)this.onclick();}}
const els={};for(const id of ['location','preset','fields','config','error','apply','download','load','results','summary','plot','starter'])els[id]=new Element();
els.starter.textContent=starter;els.preset.value='FM';let blob;
const context={document:{getElementById:id=>els[id],createElement:()=>new Element(),createElementNS:()=>new Element()},Blob,URL:{createObjectURL:b=>{blob=b;return 'fixture';},revokeObjectURL:()=>{}},setTimeout:fn=>fn()};
vm.runInNewContext(script,context);
els.location.value='catcher';els.preset.value='CHIRP';els.carrier_Hz.value='900';els.apply.onclick();
let c=JSON.parse(els.config.value);assert.equal(c.acoustic.location,'catcher');assert.equal(c.acoustic.carrier_Hz,900);assert.equal(c.acoustic.waveform,'linear_chirp');
els.download.onclick();assert(blob);
els.preset.value='OFF';els.apply.onclick();c=JSON.parse(els.config.value);assert.equal(c.acoustic.arm,'OFF');assert.equal(c.acoustic.driver_wall_J,0);
(async()=>{const exportText=await blob.text();JSON.parse(exportText);if(process.argv[3])fs.writeFileSync(process.argv[3],exportText,{flag:'wx'});await els.results.onchange({target:{files:[{text:async()=>JSON.stringify({status:'fixture',physical_prediction:'BLOCKED',integrated_extensions:{acoustic:{status:'SYNTHETIC',trace:[[-1,0,0,0],[0,0,1e-6,0]]}}})}]}});assert(els.summary.textContent.includes('BLOCKED'));assert.equal(els.plot.children.length,2);assert.equal(els.error.textContent,'');console.log(JSON.stringify({status:'PASS',scope:'DOM_EVENT_HARNESS_NOT_BROWSER_RENDERING',checks:['embedded script parses','location/frequency/chirp binding','configuration JSON download','OFF zero drive preset','result viewer/chart data binding']}));})();
