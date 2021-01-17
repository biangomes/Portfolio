<div class="titulo" center azul>Integracao css</div>

<h1 center>
<?php
echo "Olá";
//echo "<small>";
echo " Mundo";
//echo "</small>";
?>
</h1>

<?= "<div  center>Outra forma de me 'expressar'!</div>" ?>

<br>
<div center><button dobro><?= "Legal" ?></button></div>

<style>
    button {
        padding: 5px 20px;
        background-color: #4286f4;
        color: #EEE;
        font-weight: bold;
        border-radius: 10px;
    }

    [center] {
        display: flex;
        justify-content: center;
    }

    [azul] {
        color: #4286f4;
    }

    [dobro] {
        font-size: 2rem;
    }
</style>