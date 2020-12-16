use std::convert::TryFrom;

#[derive(Clone, Copy, PartialEq, Debug)]
enum Position {
    Floor,
    Empty,
    Occupied,
}

impl TryFrom<char> for Position {
    type Error = std::io::Error;
    fn try_from(c: char) -> Result<Self, Self::Error> {
        use std::io::Error;
        use std::io::ErrorKind::InvalidInput;
        match c {
            '.' => Ok(Position::Floor),
            'L' => Ok(Position::Empty),
            '#' => Ok(Position::Occupied),
            _ => Err(Error::new(InvalidInput, "Invalid seats")),
        }
    }
}

type Layout = Vec<Vec<Position>>;

fn read_input() -> Result<Layout, std::io::Error> {
    use std::fs::File;
    use std::io::{BufRead, BufReader, Error};

    let file = File::open("input.txt")?;
    let buffer = BufReader::new(file);
    let layout: Result<Layout, Error> = buffer
        .lines()
        .map(|line| line.map(|l| l.chars().map(Position::try_from).collect()))
        .flatten()
        .collect();
    layout
}

fn adjacent_seats(i: usize, j: usize, layout: &Layout) -> usize {
    if layout.is_empty() || layout[0].is_empty() {
        return 0;
    }

    let i = i as isize;
    let j = j as isize;

    let mut count = 0;
    for di in -1isize..=1 {
        for dj in -1isize..=1 {
            let ei = i + di;
            let ej = j + dj;
            if !(di == 0 && dj == 0)
                && 0 <= ei
                && ei < layout.len() as isize
                && 0 <= ej
                && ej < layout[0].len() as isize
                && matches!(layout[ei as usize][ej as usize], Position::Occupied)
            {
                count += 1;
            }
        }
    }
    count
}

fn first_see_seats(i: usize, j: usize, layout: &Layout) -> usize {
    if layout.is_empty() || layout[0].is_empty() {
        return 0;
    }

    let i = i as isize;
    let j = j as isize;

    let mut count = 0;
    for di in -1isize..=1 {
        for dj in -1isize..=1 {
            if di == 0 && dj == 0 {
                continue;
            }
            let mut r = 1;
            loop {
                let seat;
                let ei = i + r * di;
                let ej = j + r * dj;
                if 0 <= ei && ei < layout.len() as isize && 0 <= ej && ej < layout[0].len() as isize
                {
                    seat = layout[ei as usize][ej as usize];
                } else {
                    break;
                }
                match seat {
                    Position::Occupied => {
                        count += 1;
                        break;
                    }
                    Position::Empty => {
                        break;
                    }
                    _ => (),
                };
                r += 1;
            }
        }
    }
    count
}

fn exec_round(
    current: &Layout,
    new: &mut Layout,
    tolerance: usize,
    neighbor_function: fn(usize, usize, &Layout) -> usize,
) -> bool {
    assert_eq!(current.len(), new.len());
    assert_eq!(current[0].len(), new[0].len());
    let mut change = false;
    for (i, row) in current.iter().enumerate() {
        for (j, seat) in row.iter().enumerate() {
            new[i][j] = match (seat, neighbor_function(i, j, &current)) {
                (Position::Empty, 0) => {
                    change = true;
                    Position::Occupied
                },
                (Position::Occupied, n) if n >= tolerance => {
                    change = true;
                    Position::Empty
                }
                _ => *seat,
            };
        }
    }

    change
}

fn main() -> Result<(), std::io::Error> {
    let mut layout = read_input()?;
    let original = layout.clone();
    let mut other = layout.clone();

    while exec_round(&layout, &mut other, 4, adjacent_seats) {
        std::mem::swap(&mut layout, &mut other);
    }

    let count = layout
        .iter()
        .flatten()
        .filter(|p| matches!(p, Position::Occupied))
        .count();
    println!("{}", count);

    layout = original;
    while exec_round(&layout, &mut other, 5, first_see_seats) {
        std::mem::swap(&mut layout, &mut other);
    }

    let count = layout
        .iter()
        .flatten()
        .filter(|p| matches!(p, Position::Occupied))
        .count();
    println!("{}", count);

    Ok(())
}
