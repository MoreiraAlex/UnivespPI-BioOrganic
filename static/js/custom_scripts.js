
// CEP

$("#id_cep").blur(function(){
    // Remove tudo o que não é número para fazer a pesquisa
    var cep = this.value.replace(/[^0-9]/, "");
    
    // Validação do CEP; caso o CEP não possua 8 números, então cancela
    // a consulta
    if(cep.length != 8){
        return false;
    }
    
    // A url de pesquisa consiste no endereço do webservice + o cep que
    // o usuário informou + o tipo de retorno desejado (entre "json",
    // "jsonp", "xml", "piped" ou "querty")
    var url = "https://viacep.com.br/ws/"+cep+"/json/";
    
    // Faz a pesquisa do CEP, tratando o retorno com try/catch para que
    // caso ocorra algum erro (o cep pode não existir, por exemplo) a
    // usabilidade não seja afetada, assim o usuário pode continuar//
    // preenchendo os campos normalmente
    $.getJSON(url, function(dadosRetorno){
        try{
            // Preenche os campos de acordo com o retorno da pesquisa
            $("#id_address").val(dadosRetorno.logradouro);
            $("#id_block").val(dadosRetorno.bairro);
            $("#id_city").val(dadosRetorno.localidade);
            $("#id_uf").val(dadosRetorno.uf);
        }catch(ex){}
    });
});




//COOKIES


var purecookieTitle="Cookies";
var purecookieDesc="Este site utiliza cookies para te proporcionar uma melhor experiência. Ao continuar navegando, você aceita nossa";
var purecookieLink='<a href="/privacy" target="_blank">Politica de Privacidade</a>';
var purecookieButton="Aceito";

function pureFadeIn(e,o){
    var i= document.getElementById(e);
    i.style.opacity = 0;
    i.style.display= o || "block",

    function e(){
        var o = parseFloat(i.style.opacity);
        (o += .02) > 1 || (i.style.opacity = o, requestAnimationFrame(e))
    }()
}

function pureFadeOut(e){
    var o = document.getElementById(e);
    o.style.opacity = 1,

    function e(){
        (o.style.opacity -= .02) <0 ? o.style.display="none":requestAnimationFrame(e)
    }()
}

function setCookie(e,o,i){
    var t = "";
    
    if(i){   
        var n = new Date;

        n.setTime(n.getTime()+24*i*60*60*1e3);
        t = "; expires=" + n.toUTCString();
    }
    
    document.cookie = e + "=" + (o || "") + t + "; path=/"
}

function getCookie(e){
    for(var o = e + "=", i=document.cookie.split(";"), t=0;t<i.length;t++){
        for(var n = i[t];" " == n.charAt(0);)
            n = n.substring(1, n.length);

        if(0 == n.indexOf(o))
            return n.substring(o.length, n.length)
    }
    
    return null
}

function eraseCookie(e){
    document.cookie = e + "=; Max-Age=-99999999;"
}

function cookieConsent(){
    getCookie("purecookieDismiss") || (document.body.innerHTML += '<div class="cookieConsentContainer" id="cookieConsentContainer"><div class="cookieTitle"><a>'+purecookieTitle+'</a></div><div class="cookieDesc"><p>'+purecookieDesc+" "+purecookieLink+'</p></div><div class="cookieButton"><a onClick="purecookieDismiss();">'+purecookieButton+"</a></div></div>",pureFadeIn("cookieConsentContainer"))}

function purecookieDismiss(){
    setCookie("purecookieDismiss","1",7)
    pureFadeOut("cookieConsentContainer")
}

window.onload = function(){
    cookieConsent()
}
