let fibs = [];

function fibo(n) {
  if (fibs[n]) {
    return fibs[n];
  }
  if (n <= 1) {
    fibs[n] = n;
    return n;
  }

  const fib = fibo(n - 1) + fibo(n - 2);
  fibs[n] = fib
  console.log("fibo of", n, "is", fib);
  return fib;
}

fibo(7);
