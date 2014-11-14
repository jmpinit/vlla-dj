function play(file) {
    $.post("ctrl/" + file, function(data) {
        alert(data);
    });
}
