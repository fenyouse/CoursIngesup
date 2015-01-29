<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

require_once '/autoload.inc.php';

/**
 * Description of Album
 *
 * @author mmaldo
 */
class Album implements Iterator{
    private $dateParution;
    private $titre;
    private $artiste;
    private $jaquette;
    private $LesPistes;
    
    public function __construct ()
    {   
        if (func_num_args()> 0)
        {
            $this->dateParution = func_get_arg(0);
            $this->titre =func_get_arg(1);
            $this->artiste = func_get_arg(2);
            $this->jaquette =func_get_arg(3);
            $this->lesPistes = array ();      
        }
        else
           $this->lesPistes = array ();   
    }

    public function getAnneeDeParution () { return $this->$dateParution; }    
    public function getTitre () { return $this->titre; }
    public function getArtistre () { return $this->artiste; }
    public function getJacquette () { return $this->jaquette; }
    
    public function ajouterPiste (Piste $p_laPiste)
    {       
        $this->lesPistes[] = $p_laPiste;
    }      
    
    /* implementation de l'interface Iterator */    
    public function current () 
    {
        return current ($this->lesPistes);
    }
    public function key ()
    {
        return key($this->lesPistes);
    }
    public function next  ()
    {
       next($this->lesPistes);
    }
            
    public function rewind ()
    {
        reset($this->lesPistes);
    }
    public function valid ()
    {
        return (key($this->lesPistes) !== NULL);
    }
        
    public function getDuree ()
    {
        $temps = $this->getDureeEnSec ();
        $min = intval($temps / 60);
        $sec = $temps % 60;
               
        return Piste::surDeuxChiffres($min) . ":" . Piste::surDeuxChiffres($sec);
    }

    public function getDureeEnSec ()
    {
        $duree = 0;
        foreach ($this as $unePiste)
          $duree += $unePiste->getDureeEnSec ();
        
        return $duree;
    }   
}
