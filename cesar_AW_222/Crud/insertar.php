<?php

include("conexion.php");

$con = conectar();

/*RECIBIR LA INFORMACION DEL FORMULARIO*/
$matricula = $_POST['matricula'];
$nombre = $_POST['nombre'];
$apellido_p = $_POST['apellido_p'];
$apellido_m = $_POST['apellido_m'];
$edad = $_POST['edad'];

/*CONSTRUIMOS LA CONSULTA PARA INSERTAR LA INFORMACION */
$sql = "INSERT INTO alumnos (matricula, nombre, apellido_p, apellido_m, edad)
VALUES
('$matricula','$nombre', '$apellido_p', '$apellido_m', '$edad')";

/*EJECUTAMOS EN LA CONSOLA*/
$query = mysqli_query($con,$sql);

if($query){
    header("Location: alumnos.php");
}
    else{
        echo"Error al insertar el alumno";

    }






?>