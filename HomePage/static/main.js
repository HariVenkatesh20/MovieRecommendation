let slideIndex = 0;
  showSlides();
    
  function showSlides() {
      let i;
      let slides = document.getElementsByClassName("mySlides");
      let d = document.getElementsByClassName("mySlides");
      for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
      }
      slideIndex++;
      if (slideIndex > slides.length) {slideIndex = 1}    
      for (i = 0; i < d.length; i++) {
        d[i].className = d[i].className.replace(" active", "");
      }
      slides[slideIndex-1].style.display = "block";  
      d[slideIndex-1].className += " active";
      setTimeout(showSlides, 4000); // Change image every 4 seconds
  }

/*$(document).ready(function() {
    $('#search-input').keyup(function() {
        var query = $(this).val();
        if (query.length > 0) {
            $.ajax({
                url: '/suggest/',
                method: 'GET',
                data: { 'q': query },
                success: function(data) {
                    $('#suggestions').html(data);
                }
            });
        } else {
            $('#suggestions').empty();
        }
    });
});*/
