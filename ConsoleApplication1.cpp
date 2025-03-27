#include <iostream>
using namespace std;

int main() {
    double a, b;
    string answer;
    int score = 0;

    cout << "Enter number a: ";
    cin >> a;
    cout << "Enter number b: ";
    cin >> b;

    cout << "Calculation results:\n";
    cout << "a + b = " << (a + b) << "\n";
    cout << "a - b = " << (a - b) << "\n";
    cout << "a * b = " << (a * b) << "\n";

    if (b != 0) {
        cout << "a / b = " << (a / b) << "\n";
    }
    else {
        cout << "a / b = Error: Division by zero\n";
    }

    cout << "\nQuestion 1: What is the high of Everest?\n";
    cout << "a) 8967\n";
    cout << "b) 8849\n";
    cout << "c) 7946\n";
    cout << "d) 8834\n";
    cout << "Your answer: ";
    cin >> answer;
    if (answer == "b") {
        score++;
    }
    else {
        cout << "Wrong answer! Game over.\n";
        return 0;
    }

    cout << "\nQuestion 2: What is the capital of Ukraine?\n";
    cout << "a) Paris\n";
    cout << "b) London\n";
    cout << "c) Kyiv\n";
    cout << "d) Moscow\n";
    cout << "Your answer: ";
    cin >> answer;
    if (answer == "c") {
        score++;
    }
    else {
        cout << "Wrong answer! Game over.\n";
        return 0;
    }

    cout << "\nQuestion 3: Who created C++?\n";
    cout << "a) Elon Musk\n";
    cout << "b) Guido van Rossum\n";
    cout << "c) Benjamin Franklin\n";
    cout << "d) Bjarne Stroustrup\n";
    cout << "Your answer: ";
    cin >> answer;
    if (answer == "d") {
        score++;
    }
    else {
        cout << "Wrong answer! Game over.\n";
        return 0;
    }

    cout << "\nQuestion 4: What is the largest planet in our solar system?\n";
    cout << "a) Earth\n";
    cout << "b) Mars\n";
    cout << "c) Jupiter\n";
    cout << "d) Saturn\n";
    cout << "Your answer: ";
    cin >> answer;
    if (answer == "c") {
        score++;
    }
    else {
        cout << "Wrong answer! Game over.\n";
        return 0;
    }

    cout << "\nQuestion 5: How many stars on the American flag?\n";
    cout << "a) 49\n";
    cout << "b) 50\n";
    cout << "c) 51\n";
    cout << "d) 48\n";
    cout << "Your answer: ";
    cin >> answer;
    if (answer == "b") {
        score++;
    }
    else {
        cout << "Wrong answer! Game over.\n";
        return 0;
    }

    if (score == 5) {
        cout << "Congratulations! You've won the game!\n";
    }

    string responses[] = {
        "Yes", "Absolutely", "Of course", "Definitely", "Without a doubt",
        "No", "Absolutely not", "Never", "I don't think so", "Impossible",
        "Maybe", "Hard to say", "Ask again later", "Uncertain", "Not sure",
        "Possibly", "Try again", "It depends", "Not clear", "Who knows"
    };

    cout << "Molfar 4000: Ask me any question!\n";
    string question;
    cout << "Answer: " << responses[rand() % 20] << "\n";

    return 0;
}