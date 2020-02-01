$(document).ready(function(){
  
    /* 1. Visualizing things on Hover - See next part for action on click */
    $('#stars li').on('mouseover', function(){
      var onStar = parseInt($(this).data('value'), 10); // The star currently mouse on
     
      // Now highlight all the stars that's not after the current hovered star
      $(this).parent().children('li.star').each(function(e){
        if (e < onStar) {
          $(this).addClass('hover');
        }
        else {
          $(this).removeClass('hover');
        }
      });
      
    }).on('mouseout', function(){
      $(this).parent().children('li.star').each(function(e){
        $(this).removeClass('hover');
      });
    });
    
    
    /* 2. Action to perform on click */
    // $('#stars li').on('click', function(){
    //     var onStar = parseInt($(this).data('value'), 10); // The star currently selected
    //     var stars = $(this).parent().children('li.star');
    //     for (i = 0; i < stars.length; i++) {
    //         $(stars[i]).removeClass('selected');
    //     }
    //     for (i = 0; i < onStar; i++) {
    //         $(stars[i]).addClass('selected');
    //     }
    //     // JUST RESPONSE (Not needed)
    //     var ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
    //     var rating_div = document.getElementsByClassName('rating_value')
     
    //     $('#rating_value').val(ratingValue)

    //     console.log("THis is the rating of the recommendation : ", ratingValue)
      
    // });
    

    // var elements = document.getElementById("my-form").elements;
    // var elements = document.querySelectorAll("#my-form input[type=hidden]")
    // console.log(elements)
  //   elements.forEach((eachElement, i)=>{
  //     let ratingValue;
  //     $('#stars li').on('click', function(){

  //       var onStar = parseInt($(this).data('value'), 10); // The star currently selected
  //       var stars = $(this).parent().children('li.star');
  //       for ( let j = 0; j < stars.length; j++) {
  //           $(stars[j]).removeClass('selected');
  //       }
  //       for ( let k = 0; k < onStar; k++) {
  //           $(stars[k]).addClass('selected');
  //       }
  //       // JUST RESPONSE (Not needed)
  //       ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
     
  //       eachElement.setAttribute("value", ratingValue);

        
  //   })

  // });  
//   $('#stars li').on('click',function(){
//     	var onStar = parseInt($(this).data('value'), 10); // The star currently selected
// 		var stars = $(this).parent().children('li.star');
		
//         for ( let j = 0; j < stars.length; j++) {
//             $(stars[j]).removeClass('selected');
//         }
//         for ( let k = 0; k < onStar; k++) {
//             $(stars[k]).addClass('selected');
//         }
//         ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
// 		console.log("to confirm if your code will run ",$(this).parents('.rating-stars ').children("input"));
		
//     	// $(this).parents('.rating-stars').children("input").val(ratingValue);
//   })
  const starsLi = document.querySelectorAll('#stars li');
    starsLi.forEach((eachStarLi)=>{
      eachStarLi.addEventListener("click",()=>{
      var onStar = parseInt($(eachStarLi).data('value'), 10); // The star currently selected
      var stars = $(eachStarLi).parent().children('li.star');
      
          for ( let j = 0; j < stars.length; j++) {
              $(stars[j]).removeClass('selected');
          }
          for ( let k = 0; k < onStar; k++) {
              $(stars[k]).addClass('selected');
          }
          ratingValue = parseInt($('#stars li.selected').last().data('value'), 10);
      console.log("to confirm if your code will run ",$(eachStarLi).parent().parent().children("input"));
      $(eachStarLi).parent().parent().children("input").val(ratingValue);
      })
    })
});
  