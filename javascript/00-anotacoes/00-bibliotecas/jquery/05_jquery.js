/*
 * JQuery é uma biblioteca de funções JavaScript que interage com o HTML, desenvolvida para simplificar os scripts interpretados no navegador do cliente (client-side).
 * É uma biblioteca gratuita, de código aberto e de alta performance.
 *
 * npm install jquery
 */

/*
	<!-- jQuery -->
	<script src="jquery-3.7.0.min.js"></script>

	<!-- Script -->
	<script>

		// Ao carregar o documento
		$(document).ready(function(){
			// Códigos
		});

	</script>
*/


// SELETORES

{/* <body>
	<input type="text" value="Campo Nome">
	<h1 id="titulo">Título em H!</h1>
	<h2 class="subtitulo">Título em H2</h2>
</body> */}

$(document).ready(function(){
	var campo = $("input").val();
	var titulo = $("#titulo").html();
	var subtitulo = $(".subtitulo").html();

	alert(campo);
	alert(titulo);
	alert(subtitulo);
});


// EVENTOS

{/* <body>
	<h1></h1>
	<button>Clique aqui</button>
</body> */}

$(document).ready(function(){
	$("button").click(function(){
		$("h1").html("Você clicou no botão!");
	});
});


// EXIBIR E OCULTAR

{/* <body>
	<button id="exibir">Exibir</button>
	<button id="ocultar">Ocultar</button>
	<h1>Agora você me vê</h1>
</body> */}

$(document).ready(function(){
	$("#ocultar").click(function(){
		$("h1").hide();
	});
	$("#exibir").click(function(){
		$("h1").show();
	});
});


// FADE IN E FADE OUT

{/* <body>
	<button id="exibir">Exibir</button>
	<button id="ocultar">Ocultar</button>
	<hr>
	<h1>Aprendendo jQuery</h1>
</body> */}

$(document).ready(function(){
	$("h1").css("display", "none");
	$("#exibir").click(function(){
		// $("h1").fadeIn();
		$("h1").fadeIn("slow");
	});
	$("#ocultar").click(function(){
		// $("h1").fadeOut();
		$("h1").fadeOut(3000);
	});
});


// SLIDE

{/* <body>
	<h1 class="exibir">Exibir</h1>
	<h1 class="ocultar">Ocultar</h1>
	<hr>
	<h1 class="mensagem">Olá!</h1>
</body> */}

$(document).ready(function(){
	$(".ocultar").click(function(){
		// $(".mensagem").slideUp();
		$(".mensagem").slideUp(1500);
	});
	$(".exibir").click(function(){
		// $(".mensagem").slideDown();
		$(".mensagem").slideDown(1500);
	});
});


// ANIMATE

{/* <style>
	div{
		width: 100px;
		height: 80px;
		background-color: thistle;
	}
</style> */}

{/* <body>
	<button>Clique aqui</button>
	<div></div>
</body> */}

$(document).ready(function(){
	$("button").click(function(){
		$("div").animate({
			width: '400px',
			opacity: '0.5'
		});
	});
});


// CSS

{/* <body>
	<h1>Utilizando CSS com jQuery</h1>
</body> */}

$(document).ready(function(){
	$("h1").css({
		"color": "red",
		"border": "1px solid black",
		"background-color": "yellow"
	});
});


// ALTERAR ATRIBUTOS

{/* <body>
	<h1>Utilizando CSS com jQuery</h1>
</body> */}

$(document).ready(function(){
	$("h1").attr("style", "color: red; font-size: 50px;");
	$("h1").attr("title", "Este é um <h1>");
});
