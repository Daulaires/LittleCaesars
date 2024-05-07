(function(){

document.getElementById('createAccountForm').addEventListener('submit',function(event){event.preventDefault();const formData=new FormData(this);const email=formData.get('email');const password=formData.get('password');const U='/v1/create';const rB=JSON.stringify({email:email,password:password});const pH={'Content-Type':'application/json'};fetch(U,{method:'POST',headers:pH,body:rB}).then(async r=>{if(r.ok){sN('Account created for '+email,'Success');return r.json();}else{const text=await r.text();sN('Error: '+text,'Error');throw new Error(text);}});});
function hS(event){event.preventDefault();const formData=new FormData(this);const email=formData.get('email');const times=formData.get('times');const rB=cRB(email,times);const U='/v1/spam';sPR(U,rB).then(async r=>{if(r.ok){sN(email+' '+times+' times','Success');return r.json();}else{const text=await r.text();sN('Error: '+text,'Error',document.body);throw new Error(text);}});}
function cRB(email,times){return JSON.stringify({email:email,times:times});}
function sPR(U,rB){const pH={'Content-Type':'application/json'};const fU='http://127.0.0.1:999'+U;return fetch(fU,{method:'POST',headers:pH,body:rB});}
document.getElementById('spamForm').addEventListener('submit',hS);
document.addEventListener('DOMContentLoaded',function(){const mTB=document.getElementById('menuToggle');const mC=document.getElementById('menu');function uBT(){if(mC.style.display==='none'){mTB.textContent='Show Menu';}else{mTB.textContent='Hide Menu';}}
function sM(){setTimeout(function(){mC.classList.remove('hide');mC.classList.add('show');mC.style.display='block';},100);}
function hM(){setTimeout(function(){mC.classList.add('hide');},500);setTimeout(function(){mC.style.display='none';},1000);}
function hMT(){if(mC.style.display==='none'){sM();}else{hM();}
setTimeout(function(){uBT();},1000);}
uBT();mTB.addEventListener('click',hMT);});
document.addEventListener('DOMContentLoaded',function(){const tCAFB=document.getElementById('toggleCreateAccountForm');const cAFE=document.getElementById('createAccountForm');function uBT(){if(cAFE.style.display==='none'){tCAFB.textContent='Show Create Account';}else{tCAFB.textContent='Hide Create Account';}}
uBT();tCAFB.addEventListener('click',function(){if(cAFE.style.display==='none'){cAFE.classList.remove('hide');cAFE.style.display='block';}else{setTimeout(function(){cAFE.classList.add('hide');},500);setTimeout(function(){cAFE.style.display='none';},1000);}
setTimeout(function(){uBT();},1000);});});
document.addEventListener('DOMContentLoaded',function(){const tSFB=document.getElementById('toggleSpamForm');const sFE=document.getElementById('spamForm');function uBT(){if(sFE.style.display==='none'){tSFB.textContent='Show Spam Form';}else{tSFB.textContent='Hide Spam Form';}}
uBT();tSFB.addEventListener('click',function(){if(sFE.style.display==='none'){sFE.classList.remove('hide');sFE.style.display='block';}else{setTimeout(function(){sFE.classList.add('hide');},500);setTimeout(function(){sFE.style.display='none';},1000);}
setTimeout(function(){uBT();},1000);});});
document.addEventListener('DOMContentLoaded',function(){const RAB=document.getElementById('RandomAccount');const rAB=document.body;RAB.addEventListener('click',function(){const U='/v1/create_account_with_random_data';fetch(U,{method:'GET'}).then(async r=>{if(r.ok){const data=await r.json();sN('Account: '+JSON.stringify(data),'Success',rAB);return data;}else{const text=await r.text();sN('Error: '+text,'Error',rAB);throw new Error(text);}}).catch(error=>{('Error:',error);sN('Error: '+error.m,'Error',rAB);});});});
document.addEventListener('DOMContentLoaded',function(){const pDM=window.matchMedia('(prefers-color-scheme: dark)').matches;const tB=document.getElementById('themeToggle');const body=document.body;function uBT(){if(pDM){body.classList.remove('light-mode');body.classList.add('dark-mode');}else{body.classList.remove('dark-mode');body.classList.add('light-mode');}
if(body.classList.contains('dark-mode')){tB.textContent='Light Mode';}else{tB.textContent='Dark Mode';}}
uBT();tB.addEventListener('click',function(){if(body.classList.contains('dark-mode')){body.classList.remove('dark-mode');body.classList.add('light-mode');}else{body.classList.remove('light-mode');body.classList.add('dark-mode');}
uBT();});});
sN=(m)=>{const nC=document.getElementById('notificationContainer');const N=document.createElement('div');N.className='notification';N.textContent=m;N.style.width='auto';N.style.height='auto';nC.appendChild(N);const style=window.getComputedStyle(N);N.style.width=`${style.width}px`;N.style.height=`${style.height}px`;N.classList.add('show');setTimeout(()=>{N.classList.add('hide');},5000);setTimeout(()=>{N.classList.remove('show');nC.removeChild(N);},10000);}
uD=function(){fetch('/v1/get_accounts_created_count').then(r=>r.json()).then(data=>{aC=data.total_accounts_created;sN('Accounts created: '+aC,'Success');});}
uD();
gGTC=function(){fetch('/v1/get_global_spam_count').then(r=>r.json()).then(data=>{gTC=data.total_spam_count;sN('Spam count: '+gTC,'Success');});}
gGTC();
})();