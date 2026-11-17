const CACHE='little-learners-v9';
const FILES=['./','./index.html','./manifest.webmanifest','./content/activities.json','./icons/icon.svg','./icons/icon-180.png','./icons/icon-192.png','./icons/icon-512.png'];
self.addEventListener('install',event=>event.waitUntil(caches.open(CACHE).then(cache=>cache.addAll(FILES))));
self.addEventListener('activate',event=>event.waitUntil(caches.keys().then(keys=>Promise.all(keys.filter(key=>key!==CACHE).map(key=>caches.delete(key))))));
self.addEventListener('fetch',event=>{
  const activitiesURL=new URL('./content/activities.json',self.registration.scope);
  if(event.request.method==='GET'&&new URL(event.request.url).pathname===activitiesURL.pathname){
    event.respondWith(fetch(event.request).then(response=>{
      if(!response.ok)throw new Error('Content fetch failed');
      const copy=response.clone();
      caches.open(CACHE).then(cache=>cache.put(activitiesURL,copy));
      return response;
    }).catch(()=>caches.match(activitiesURL)));
    return;
  }
  event.respondWith(caches.match(event.request).then(cached=>cached||fetch(event.request).then(response=>{const copy=response.clone();caches.open(CACHE).then(cache=>cache.put(event.request,copy));return response}).catch(()=>caches.match('./index.html'))));
});
