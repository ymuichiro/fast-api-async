// const readline = require("readline");

async function fetcher() {
  const response = await fetch("http://localhost:8000/");

  if (response.status === 200) {
    const stream = response.body;
    const reader = stream.getReader();
    while (true) {
      const { done, value } = await reader.read();

      if (done) {
        break;
      }

      // result += new TextDecoder().decode(value);
      // readline.cursorTo(process.stdout, 0);
      // process.stdout.write(`result: ${result}`);
    }
    // process.stdout.write("\n");
    // process.exit();
    return true;
  } else {
    console.log(response.status);
  }
}

async function main() {
  const res = await Promise.all(new Array(3000).fill(0).map(fetcher));
  console.log(res.filter((e) => e).length);
}

main();
