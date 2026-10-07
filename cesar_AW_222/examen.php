<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Examen 1er Parcial - Aplicaciones Web</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f9;
            padding: 20px;
            display: flex;
            justify-content: center;
        }

        .examen-container {
            width: 100%;
            max-width: 900px;
            border: 2px solid #000;
            padding: 15px;
            display: flex;
            flex-direction: column;
            gap: 15px;
            background-color: #ffffff;
        }

        .box {
            border: 1px solid #000;
            padding: 15px;
            text-align: center;
        }

        .header {
            background-color: #d1ecf1;
            font-size: 1.2rem;
            font-weight: bold;
        }

        .middle-section {
            display: flex;
            gap: 15px;
        }

        .form-box {
            background-color: #f8d7da;
            flex: 1;
            text-align: left;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
        }

        .form-box form {
            display: flex;
            flex-direction: column;
        }
        
        .form-box label {
            margin-top: 10px;
            font-size: 0.9rem;
            font-weight: bold;
        }
        
        .form-box input {
            padding: 5px;
            margin-bottom: 5px;
            border: 1px solid #000;
            border-radius: 3px;
        }
        
        .form-box button {
            margin-top: 15px;
            padding: 10px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
        }
        
        .form-box button:hover {
            background-color: #0056b3;
        }

        .table-box {
            background-color: #d4edda;
            flex: 1.5;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
            background-color: #fff;
        }
        
        th, td {
            border: 1px solid #000;
            padding: 8px;
            text-align: center;
            font-size: 0.9rem;
        }

        .resources-section {
            display: flex;
            gap: 15px;
        }

        .resource {
            flex: 1;
            font-weight: bold;
        }
        
        .r1 { background-color: #fff3cd; }
        .r2 { background-color: #e2e3e5; }
        .r3 { background-color: #cce5ff; }

        .footer-box {
            background-color: #e8dff5;
            display: flex;
            justify-content: space-between;
            align-items: center;
            text-align: center;
            padding: 20px;
        }

        .footer-text p {
            margin: 5px 0;
        }
        
        .footer-text strong {
            text-transform: uppercase;
        }

        .avatar-placeholder, .logo-placeholder {
            width: 60px;
            height: 60px;
            border: 2px solid #000;
            border-radius: 50%;
            display: block;
            object-fit: cover;
            background-color: #fff;
        }
    </style>
</head>
<body>

    <div class="examen-container">

        <div class="box header">
            EXAMEN 1ER PARCIAL - APLICACIONES WEB
        </div>

 
        <div class="middle-section">
            <div class="box form-box">
                <p style="text-align: center; margin-top: 0; font-weight: bold;">FORMULARIO</p>
                
                <form method="POST" action="">
                    <label>- Marca</label>
                    <input type="text" name="marca" required>

                    <label>- Modelo</label>
                    <input type="text" name="modelo" required>

                    <label>- Anio</label>
                    <input type="number" name="anio" required>

                    <label>- Precio</label>
                    <input type="text" name="precio" required>

                    <button type="submit" name="agregar">Agregar a la tabla</button>
                </form>
            </div>
            
            <div class="box table-box">
                <p style="margin-top: 0; font-weight: bold;">TABLA DE CARROS</p>
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>MARCA</th>
                            <th>MODELO</th>
                            <th>Anio</th>
                            <th>PRECIO</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                        
                        if(isset($_POST['agregar'])) {
                            $marca_nueva = htmlspecialchars($_POST['marca']);
                            $modelo_nuevo = htmlspecialchars($_POST['modelo']);
                            $anio_nuevo = htmlspecialchars($_POST['anio']);
                            $precio_nuevo = htmlspecialchars($_POST['precio']);
                            
                            echo "<tr>
                                    <td>1</td>
                                    <td>$marca_nueva</td>
                                    <td>$modelo_nuevo</td>
                                    <td>$anio_nuevo</td>
                                    <td>$$precio_nuevo</td>
                                  </tr>";
                        }
                        ?>
                    </tbody>
                </table>
            </div>
        </div>

       
        <div class="resources-section">
            <div class="box resource r1">
                R1 - Introduccion a Git y GitHub<br><br>
                <a href="https://classroom.google.com/u/1/c/ODc3Mjc3OTg0NTA2/a/ODg0NDIzODMxODY2/details?hl=es" target="_blank">URL</a>
            </div>
            <div class="box resource r2">
                R2 - HTML + CSS + Box Model<br><br>
                <a href="https://classroom.google.com/u/1/c/ODc3Mjc3OTg0NTA2/a/ODg2MDI4Mjk4OTQ1/details?hl=es" target="_blank">URL</a>
            </div>
            <div class="box resource r3">
                R3 - Flex y Grid<br><br>
                <a href="https://classroom.google.com/u/1/c/ODc3Mjc3OTg0NTA2/a/ODg3ODgzNDUwMjAx/details?hl=es" target="_blank">URL</a>
            </div>
        </div>

        <div class="box footer-box">
            <img src="img/k8b970dsaejg1.jpeg" class="avatar-placeholder" alt="Foto de Cesar">
            
            <div class="footer-text">
                <p>-------- <strong>CESAR OSVALDO CALDERON ARIAS</strong> --------</p>
                <p>Mis 4 cuatris han sido de muchas experiencias que me an ayudado bastante y entendido que me falta mucho por aprender</p>
            </div>
            
            <img src="img/images.png" class="logo-placeholder" alt="Logo UPQ" style="padding: 5px; object-fit: contain;">
        </div>

    </div>

</body>
</html>