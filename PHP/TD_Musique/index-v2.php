<?php
require_once ("/autoload.inc.php");

try {
    // parametre ?
    if (! isset($_GET["ID"])) 
       throw new Exception ("ID de l'album en parametre de la page manquant !");
    
    // connexion à la base de données
    $db = new PDO ('mysql:host=localhost; dbname=cdbase', 'root', '');
     
    // la requete pour récuperer l'album 
    $requeteAlbum = "SELECT  Al.dateParution, Al.titre, Ar.nom, Al.jaquette "
                 .  "FROM    album Al "
                 .  "            inner join artiste Ar on (Al.IDArtiste = Ar.ID) "
                 .  "WHERE   Al.ID = " . $_GET["ID"];
    
    // l'execution 
    $res = $db->query($requeteAlbum);
    
    if (!($ligneAlbum = $res->fetch(PDO::FETCH_ASSOC)))
        throw new Exception ("Album inexistant !!");
    else
    {
        $unAlbum = new Album ($ligneAlbum["dateParution"], $ligneAlbum["titre"], $ligneAlbum["nom"], $ligneAlbum["jaquette"]);
         
        // TODO
        // récupération des pistes de cet album (requete)
        // creation des objets pistes et ajout à l'album
        $requetePistes = "SELECT  IDPiste, titre, duree "
                      .  "FROM    piste "                      
                      .  "WHERE   IDAlbum = " . $_GET["ID"] . " "
                      .  "ORDER BY IDPiste";
        $res = $db->query($requetePistes);
        while ($lignePiste = $res->fetch(PDO::FETCH_ASSOC))
        {
            $unePiste = new Piste ($lignePiste['IDPiste'], $lignePiste['titre'], $lignePiste['duree']);
            $unAlbum->ajouterPiste($unePiste);
        }
    } 
} 
catch (PDOException $e) {
    echo $e->getMessage();
} 
catch (Exception $e) {
    echo $e->getMessage();
}
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
