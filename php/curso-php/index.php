<!DOCTYPE html>
<html lang="en">

<head>
	<meta charset="utf-8">
	<link rel="preconnect" href="https://fonts.gstatic.com">
	<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@200&display=swap" rel="stylesheet">
	<link href="assets/css/estilo.css" rel="stylesheet">
	<title>Curso PHP</title>
</head>

<body>
	<header class="cabecalho">
		<h1>Curso PHP</h1>
		<h2>Índice dos exercícios</h2>
	</header>
	
	<main class="principal">
		<div class="conteudo">
			<nav class="modulos">
				<div class="modulo verde">
					<h3>Módulo 01</h3>
					<ul>
						<li>
							<a href="exercicio.php?dir=basico&file=ola">
								Olá PHP
							</a>
						</li>
						<li>
							<a href="exercicio.php?dir=basico&file=html">
								Integracao HTML
							</a>
						</li>
						<li>
							<a href="exercicio.php?dir=basico&file=css">
								Integracao css
							</a>
						</li>
						<li>
							<a href="exercicio.php?dir=basico&file=desafio">
								Desafio PHP
							</a>
						</li>
					</ul>	
				</div>
			</nav>
		</div>	
	</main>
	
	<footer class="rodape">
		COD3R & ALUNOS ₢ <?= date("Y"); ?>
	</footer>

</body>

</html>
