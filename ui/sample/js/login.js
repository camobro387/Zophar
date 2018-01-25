function showLogin() {
    $("#log-reg").hide();
    $('#hide').show();
    $('#log').show();
    $('#goback').show();
}

function showReg() {
    $("#log-reg").hide();
    $('#hide').show();
    $("#reg").show();
    $('#goback').show();
}

function reset() {
    $("#log-reg").show();
    $('#hide').hide();
    $("#reg").hide();
    $("#log").hide();
    $('#goback').hide();
}