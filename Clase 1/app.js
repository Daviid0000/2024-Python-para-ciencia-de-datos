//  Multipicando sin el operador *
// for (let factorial = 0; factorial <= i; factorial++) {
    
//     console.log("Multiplicación: ", factorial++)
// }
// function multiplica(c, d) {
// }

const multiplica = (c, d) => {
    
    return c > 0 ? multiplica(c-1, d) + d : 0;

  }
  console.log(
    multiplica(2,3),
    multiplica(3,4),
    multiplica(4,5),
    multiplica(5,6),
    multiplica(2,-6)
  );
// let a = 5
// let b = 10

// 15 = 3 * 5
// 15 = 5 + 5 + 5
// 15 = 3 + 3 + 3 + 3 + 3

// console.log(c)


//  Sumando sin el operador +
// let a = 5;
// let b = 10;

// console.log("Suma: ", a ^ b)