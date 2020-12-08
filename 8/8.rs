use std::collections::HashSet;
use std::fs::File;
use std::io::Read;

#[derive(Clone)]
enum Instruction {
    Acc(i32),
    Jmp(i32),
    Nop(i32),
}

fn read_input() -> Vec<Instruction> {
    let mut buf: String = String::new();
    let mut file = File::open("input.txt").expect("Cannot open file");
    file.read_to_string(&mut buf).expect("Cannot read file");
    buf.lines()
        .map(|line| {
            let mut parts = line.split(' ').take(2);
            let op = parts.next().expect("Invalid input: no operation");
            let arg = parts
                .next()
                .expect("Invalid input: no argument")
                .parse::<i32>()
                .expect("Invalid argument: cannot parse into i32");
            match op {
                "acc" => Instruction::Acc(arg),
                "jmp" => Instruction::Jmp(arg),
                "nop" => Instruction::Nop(arg),
                _ => panic!(format!("Unknown operation: {}", op)),
            }
        })
        .collect()
}

fn run_program(program: &Vec<Instruction>) -> (i32, i32) {
    let mut visited = HashSet::new();

    let mut counter: i32 = 0;
    let mut ip: i32 = 0;
    while !visited.contains(&ip) && (ip as usize) < program.len() {
        if let Some(instruction) = program.get(ip as usize) {
            visited.insert(ip);
            match instruction {
                Instruction::Acc(s) => counter += s,
                Instruction::Jmp(j) => {
                    ip += j;
                    continue;
                }
                Instruction::Nop(_) => (),
            };
            ip += 1;
        } else {
            panic!("Instruction pointer outside range");
        }
    }
    (counter, ip)
}

fn part1(program: &Vec<Instruction>) -> i32 {
    run_program(program).0
}

fn part2(program: &Vec<Instruction>) -> Option<i32> {
    let mut program = program.clone();
    let mut previous: Instruction;
    for i in 0..program.len() {
        let instruction = &program[i];
        previous = instruction.clone();
        match instruction {
            Instruction::Acc(_) => continue,
            Instruction::Jmp(j) => program[i] = Instruction::Nop(*j),
            Instruction::Nop(a) => program[i] = Instruction::Jmp(*a),
        }
        let (counter, ip) = run_program(&program);
        if ip as usize == program.len() {
            return Some(counter);
        }
        program[i] = previous;
    }
    None
}

fn main() {
    let program = read_input();
    println!("{}", part1(&program));
    println!("{}", part2(&program).unwrap());
}
