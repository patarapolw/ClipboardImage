const inputBar = document.getElementById('input-bar');
const imageCanvas = document.getElementById('image-canvas');

inputBar.value = imagePath;

inputBar.onpaste = ()=>{
  const items = (event.clipboardData || event.originalEvent.clipboardData).items;
  // console.log(items); // will give you the mime types
  for (index in items) {
    const item = items[index];
    if (item.kind === 'file') {
      const file = item.getAsFile();
      console.log(file);
      let reader = new FileReader();
      reader.onload = function(event) {
        const extension = file.type.match(/\/([a-z0-9]+)/i)[1].toLowerCase();

        let formData = new FormData();
        formData.append('file', file, file.name);
        formData.append('extension', extension);
        formData.append('mimetype', file.type);
        formData.append('submission-type', 'paste');
        formData.append('imagePath', imagePath)
        fetch('/api/images/create', {
          method: 'POST',
          body: formData
        }).then(response=>response.json())
          .then(responseJson=>{
            inputBar.value = responseJson.filename;
            imageCanvas.src = '/images?filename=' + encodeURIComponent(responseJson.filename);
          });
      };
      reader.readAsBinaryString(file);
    }
  }
}

inputBar.addEventListener("keydown", function(event) {
  imagePath = inputBar.value;
});

inputBar.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    fetch('/api/images/rename', {
      method: 'POST',
      headers: {
        "Content-Type": "application/json; charset=utf-8",
      },
      body: JSON.stringify({
        'filename': imagePath
      })
    }).then(response=>response.json())
      .then(responseJson=>{
        inputBar.value = responseJson.filename;
        imageCanvas.src = '/images?filename=' + encodeURIComponent(responseJson.filename);
      });
  }
});
