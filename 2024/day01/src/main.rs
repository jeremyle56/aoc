use std::fs;

fn solve_p1(mut l1: Vec<i32>, mut l2: Vec<i32>) {
    l1.sort();
    l2.sort();

    let res: i32 = l1.iter().zip(l2.iter()).map(|(a, b)| (a - b).abs()).sum();
    println!("Answer for Part 1: {}", res);
}

fn solve_p2(l1 : Vec<i32>, l2: Vec<i32>) {
    let res: i32 = l1.iter().map(|&a| (a * l2.iter().filter(|&b| *b == a).count() as i32)).sum();
    println!("Answer for Part 2: {}", res);
}

fn main() {
    let input = fs::read_to_string("./in.txt").unwrap();
    let lines: Vec<&str> = input.lines().collect();

    let mut l1 = Vec::new();
    let mut l2 = Vec::new();

    for line in lines {
        let values: Vec<&str> = line.split_whitespace().collect();
        l1.push(values[0].parse().unwrap());
        l2.push(values[1].parse().unwrap());
    }

    solve_p1(l1.clone(), l2.clone());
    solve_p2(l1, l2);
}