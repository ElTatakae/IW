<?php

// Definir el tamaño del tablero
$n = 8;

// Crear un arreglo bidimensional para representar el tablero
$tablero = array();
for ($i = 0; $i < $n; $i++) {
  $tablero[$i] = array();
  for ($j = 0; $j < $n; $j++) {
    $tablero[$i][$j] = 0;
  }
}

// Definir las posibles jugadas del caballo
$jugadas = array(
  array(2, 1),
  array(1, 2),
  array(-1, 2),
  array(-2, 1),
  array(-2, -1),
  array(-1, -2),
  array(1, -2),
  array(2, -1)
);

// Iniciar en la esquina superior izquierda
$i = 0;
$j = 0;
$contador = 1;
$tablero[$i][$j] = $contador;

// Realizar el ciclo hamiltoniano
for ($k = 0; $k < $n * $n - 1; $k++) {
  // Encontrar la siguiente jugada en sentido a la derecha
  $mejorJugada = -1;
  $mejorDistancia = $n + 1;
  for ($m = 0; $m < 8; $m++) {
    $ii = $i + $jugadas[$m][0];
    $jj = $j + $jugadas[$m][1];
    if ($ii >= 0 && $jj >= 0 && $ii < $n && $jj < $n && $tablero[$ii][$jj] == 0) {
      $distancia = 0;
      for ($p = 0; $p < 8; $p++) {
        $iii = $ii + $jugadas[$p][0];
        $jjj = $jj + $jugadas[$p][1];
        if ($iii >= 0 && $jjj >= 0 && $iii < $n && $jjj < $n && $tablero[$iii][$jjj] == 0) {
          $distancia++;
        }
      }
      if ($distancia < $mejorDistancia) {
        $mejorJugada = $m;
        $mejorDistancia = $distancia;
      }
    }
  }

  // Mover el caballo y marcar el salto en el tablero
  $i += $jugadas[$mejorJugada][0];
  $j += $jugadas[$mejorJugada][1];
  $contador++;
  $tablero[$i][$j] = $contador;
}

// Imprimir el tablero con los saltos del caballo enumerados
echo "<table>";
for ($i = 0; $i < $n; $i++) {
  echo "<tr>";
  for ($j = 0; $j < $n; $j++) {
    echo "<td>" . $tablero[$i][$j] . "</td>";
  }
  echo "</tr>";
}
echo "</table>";

?>
