    /* Loading At First Request */
    let spinnerWraper = document.querySelector('.spinner-wrapper');

    setTimeout(function (){
        // Something you want delayed.
            spinnerWraper.parentElement.removeChild(spinnerWraper);
      }, 700); // How long do you want the delay to be (in milliseconds)? 
    
    /* ===== Scroll to Top ====  */
    $(window).scroll(function() {
        if ($(this).scrollTop() >= 50) {        // If page is scrolled more than 50px
            $('#return-to-top').fadeIn(200);    // Fade in the arrow
        } else {
            $('#return-to-top').fadeOut(200);   // Else fade out the arrow
        }
    });
    $('#return-to-top').click(function() {      // When arrow is clicked
        $('body,html').animate({
            scrollTop : 0                       // Scroll to top of body
        }, 500);
    });
    /*DateTime*/
    var DateTimeDiv = document.getElementById('DateTime');
    var days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
    var months = ['January','February','March','April','May','June','July','August','September','October','November','December'];

    (function updateDateTime(){
        var now = new Date();
        time = now.getHours() + ':' + (now.getMinutes()<10?'0':'') + now.getMinutes();
        date = days[now.getDay()]+', '+ now.getDate() +' '+months[now.getMonth()] ;
        DateTimeDiv.innerHTML = `<span class="time">${time}</span> </br> <span class="date">${date}</span>`;
        setTimeout(updateDateTime, 10000);
    })();
    /*Location
    var LocationDiv = document.getElementById('location');
    $.getJSON("https://api.ipify.org?format=json",
        function(dataIp) {
            //Response Must be 200 otherwise leave !
                $.getJSON('https://ipapi.co/'+dataIp.ip+'/json', function(data){
                    LocationDiv.innerHTML = `
                        <img src="https://image.flaticon.com/icons/png/512/684/684908.png" width="25">
                        <!--
                        <span>${data.city} ,</span>
                        -->
                        <span>${data.country_name}</span>
                        <img src="https://whatismyipaddress.b-cdn.net/wp-content/plugins/user-ip-and-location/flags/${data.country.toLowerCase()}.png" width="25">
                    `;
                });
    });
    */
    /* Ubunto Buttons Response */
    const btnX = $('#dotX').click(function() {
        $('#section1').fadeOut("slow");
        });
    const btnO = $('#dotO').click(function() {
        if ($('#UbuntoWindow').css('max-width') == '1400px') {
            $('#UbuntoWindow').css({"max-width": "100%"});
        }else{
            $('#UbuntoWindow').css({"max-width": "1400px"});
        }
        });
    const btnMinus = $('#dot-').click(function() {
        if ($('#dotO').is(":visible")) {
            $('#dotO').fadeOut("slow");
            $('.UbuntoContent').fadeOut("slow");
        }else{
        $('#dotO').fadeIn("slow");
        $('.UbuntoContent').fadeIn("slow");
        }
        });
    /* Theme Change Handeling*/
    theme = localStorage.getItem('theme');
    let static = "static/css/"
    if(theme == null){
        setTheme('purple')
    }else{
        setTheme(theme)
    }

    let themeDots = document.getElementsByClassName('theme-dot')

    for (var i=0; themeDots.length > i; i++){
        themeDots[i].addEventListener('click', function(){
            let mode = this.dataset.mode
            setTheme(mode)
        })
    }

    function setTheme(mode){
        if(mode == 'light'){
            document.getElementById('theme-style').href = static + 'themes/light.css'
        }

        if(mode == 'blue'){
            document.getElementById('theme-style').href = static + 'themes/blue.css'
        }

        if(mode == 'green'){
            document.getElementById('theme-style').href = static + 'themes/green.css'
        }

        if(mode == 'purple'){
            document.getElementById('theme-style').href = static + 'themes/purple.css'
        }
        localStorage.setItem('theme', mode)
}

/* Image Project slider */
let projectIndex = 0;
const projects = document.querySelector(".projects-wrapper").children
for(let projectIndex=0; projectIndex<projects.length; projectIndex++){
    let index=0;
    let slides=projects[projectIndex].querySelector(".images-wrapper").children;
    function changeSlide(){
        for(let i=0; i<slides.length; i++){
            slides[i].classList.remove("is-selected");
            
        }
        slides[index].classList.add("is-selected");
    }
    
    
    function nextSlide(){
    if(index==slides.length-1){ // -1 for the list diff
        index=0;
    }
    else{
        index++;
    }
    changeSlide();
    }
    
    function autoPlay(){
    nextSlide();
    }
    
    let timer=setInterval(autoPlay,2000);
}