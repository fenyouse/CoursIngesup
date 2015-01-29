<?php

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

require_once '/autoload.inc.php';

/**
 * Description of Propriete
 *
 * @author mmaldo
 */
class Piste {
    //put your code here
    private $numero;
    private $titre;
    private $duree;
           
    public function __construct ()
    {
        if (func_num_args()> 0)
        {
            $this->numero =  func_get_arg(0);
            $this->titre = func_get_arg(1);
            $this->duree =  func_get_arg(2);
        }
    }
    
    public function getNumero () { return $this->numero; }
    public function getTitre () { return $this->titre; }
    public function getDuree () { return $this->duree; }
    public function getDureeEnSec () 
    { 
        $temps = explode(":", $this->getDuree());        
        return 60 * $temps[0] +  $temps[1];        
    }
     
    public function toString ()
    {
        return "$this->numero - $this->titre  <i>($this->duree)</i>";
    }  
    
    public static function surDeuxChiffres ($val)
    {
        return ($val < 10) ? ("0". $val) : $val;
    }
}


