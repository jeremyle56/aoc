use std::fs;

fn solve_p1(input: String) {
    println!("Answer for Part 1: {}", res);
}

fn solve_p2(input: String) {
    println!("Answer for Part 2: {}", res);
}

fn main() {
    let input = fs::read_to_string("./in.txt").expect("Unable to read file");

    solve_p1(input.clone());
    solve_p2();
}