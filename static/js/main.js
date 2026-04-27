function searchImages() {
    let query = document.getElementById('searchBox').value;
    fetch(`/search?q=${query}`)
    .then(response => response.json())
    .then(data => {
        let gallery = document.getElementById('gallery');
        gallery.innerHTML = '';
        data.forEach(item => {
            let img = document.createElement('img');
            img.src = item.url;
            img.alt = item.source;
            img.className = 'thumb';
            gallery.appendChild(img);
        });
    });
}
