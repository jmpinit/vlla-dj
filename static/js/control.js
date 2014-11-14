function play(file) {
    $.post("ctrl/" + file, function(data) {
        console.log(data);
    });
}
