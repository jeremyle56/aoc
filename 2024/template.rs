use std::fs;

fn solve_p1(input: Vec<&str>) {
    println!("Answer for Part 1: {}", input[0]);
}

fn solve_p2(input: Vec<&str>) {
    println!("Answer for Part 2: {}", input[0]);
}

fn main() {
    let input = fs::read_to_string("./in.txt").unwrap();
    let lines = input.lines().collect::<Vec<_>>();

    solve_p1(lines.clone());
    solve_p2(lines);
}