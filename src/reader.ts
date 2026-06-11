import { createInterface } from "node:readline";
import { stdin, stdout } from "node:process";

export function reader(question: string) {
  const rl = createInterface({
    input: stdin,
    output: stdout,
  });

  rl.question(question, (answer) => {
    console.log(`Your color is: ${answer}`);
    rl.close();
  });
}
