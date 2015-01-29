<?php

/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

require_once ("/autoload.inc.php");

$unAlbum = new Album (1987, "The Joshua Tree", "U2", "The_Joshua_Tree.png");
$unAlbum->ajouterPiste (new Piste(1, "Where the Streets Have No Name", "5:36"));
$unAlbum->ajouterPiste (new Piste(2, "I Still Haven't Found What I'm Looking For", "4:37"));
$unAlbum->ajouterPiste (new Piste(3, "With or Without You", "4:55"));
$unAlbum->ajouterPiste (new Piste(4, "Bullet the Blue Sky", "4:32"));
$unAlbum->ajouterPiste (new Piste(5, "Running to Stand Still", "4:17"));
$unAlbum->ajouterPiste (new Piste(6, "Red Hill Mining Town", "4:54"));
$unAlbum->ajouterPiste (new Piste(7, "In God's Country", "2:52"));
$unAlbum->ajouterPiste (new Piste(8, "Trip Through Your Wires", "3:32"));
$unAlbum->ajouterPiste (new Piste(9, "One Tree Hill", "4:43"));
$unAlbum->ajouterPiste (new Piste(10, "Exit", "4:53"));
$unAlbum->ajouterPiste (new Piste(11, "Mothers of the Disappeared", "5:12"));
?>

<!DOCTYPE html>
<html>    
    <head>
        <title><?= $unAlbum->getTitre(); ?></title>
        <meta charset="UTF-8">         
        <link rel="stylesheet" type="text/css" href="css/style.css">
    </head>
    <body>
        <div id="album">
            <span class="titreAlbum" ><?= $unAlbum->getTitre() ?></span>
            <span class="dureeAlbum">(durée <?= $unAlbum->getDuree(); ?>)</span>
            <hr />
            <img class="jacquetteAlbum" src="images/<?= $unAlbum->getJacquette() ?>"/></img>
            <ul>
            <?php foreach ($unAlbum as $unePiste) { ?>
                <li>
                    <?= $unePiste->getNumero() ?> - <span class="titrePiste"> <?= $unePiste->getTitre()?></span> ( <?= $unePiste->getDuree() ?>)
                </li>
            <?php } ?>
            </ul>
           
        </div>
    </body>   
</html>
