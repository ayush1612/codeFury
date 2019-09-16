$(document).ready(function(){
	//On click signup, hide login and show registration form
	$('#1').click(function(){
		
			$("#1.1").fadeIn("slow");
		
	});



	//On click signin, hide login and show registration form
	$('#2').click(function(){
		/*$("#avatar_div").fadeOut("slow", function(){*/
			$("#1.1").fadeOut("slow",function(){
				$("#2.1").fadeIn("slow");
			});

		});
	$('#3').click(function(){
		/*$("#avatar_div").fadeOut("slow", function(){*/
			$("#2.1").fadeOut("slow",function(){
				$("#3.1").fadeIn("slow");
			});

		});
	

	});