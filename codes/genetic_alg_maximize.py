"""Algoritmo genético para maximizar y = -x^2 - |x^3| + x^{4/3} + x/7 + 1 + 0.01 sin(100 x).
Busca soluções em x no intervalo [-1, 1].

Parâmetros do GA estão concentrados na função `run_genetic_algorithm`
para facilitar ajustes.
"""

import math
import os
import random
from dataclasses import dataclass
from typing import Callable, List, Tuple

import matplotlib.pyplot as plt
import numpy as np


def objective(x: np.ndarray) -> np.ndarray:
    """Avalia a função objetivo para um array de valores x."""
    return (
        -x ** 2
        - np.abs(x ** 3)
        + np.abs(x) ** (4.0 / 3.0)
        + x / 7.0
        + 1.0
        + 0.01 * np.sin(100.0 * x)
    )


@dataclass
class GAParams:
    population_size: int = 5
    generations: int = 20
    crossover_rate: float = 0.2
    mutation_rate: float = 0.05
    mutation_scale: float = 0.01
    tournament_size: int = 3
    elite_size: int = 2
    search_bounds: Tuple[float, float] = (-1.0, 1.0)
    random_seed: int = 42


def initialize_population(params: GAParams) -> np.ndarray:
    low, high = params.search_bounds
    return np.random.uniform(low, high, size=params.population_size)


def tournament_selection(population: np.ndarray, fitness: np.ndarray, params: GAParams) -> np.ndarray:
    selected = []
    for _ in range(params.population_size):
        competitors = np.random.choice(params.population_size, params.tournament_size, replace=False)
        winner = competitors[np.argmax(fitness[competitors])]
        selected.append(population[winner])
    return np.array(selected)


def arithmetic_crossover(parent1: float, parent2: float) -> Tuple[float, float]:
    alpha = random.random()
    child1 = alpha * parent1 + (1 - alpha) * parent2
    child2 = alpha * parent2 + (1 - alpha) * parent1
    return child1, child2


def mutate(solution: float, params: GAParams) -> float:
    if random.random() < params.mutation_rate:
        perturbation = np.random.normal(scale=params.mutation_scale)
        solution += perturbation
    low, high = params.search_bounds
    return float(np.clip(solution, low, high))


def create_new_population(selected: np.ndarray, params: GAParams) -> np.ndarray:
    next_pop = []
    random.shuffle(selected.tolist())

    for i in range(0, params.population_size - params.elite_size, 2):
        parent1 = selected[i]
        parent2 = selected[i + 1]
        if random.random() < params.crossover_rate:
            child1, child2 = arithmetic_crossover(parent1, parent2)
        else:
            child1, child2 = parent1, parent2
        next_pop.append(mutate(child1, params))
        next_pop.append(mutate(child2, params))

    if len(next_pop) > params.population_size - params.elite_size:
        next_pop = next_pop[: params.population_size - params.elite_size]

    return np.array(next_pop)


def run_genetic_algorithm(params: GAParams) -> Tuple[np.ndarray, List[float], float, float]:
    np.random.seed(params.random_seed)
    random.seed(params.random_seed)

    population = initialize_population(params)
    fitness = objective(population)
    fitness_history: List[float] = []

    for generation in range(params.generations):
        elites = population[np.argsort(fitness)[-params.elite_size :]]
        selected = tournament_selection(population, fitness, params)
        offspring = create_new_population(selected, params)
        population = np.concatenate([elites, offspring])
        fitness = objective(population)
        best_fitness = float(np.max(fitness))
        fitness_history.append(best_fitness)


        print(
            f"Geração {generation + 1}/{params.generations}: melhor fitness = {best_fitness:.6f}"
        )

    best_index = int(np.argmax(fitness))
    best_solution = float(population[best_index])
    best_value = float(fitness[best_index])
    return population, fitness_history, best_solution, best_value


def plot_results(params: GAParams, population: np.ndarray, fitness_history: List[float], best_solution: float, best_value: float) -> None:
    x_plot = np.linspace(params.search_bounds[0], params.search_bounds[1], 1000)
    y_plot = objective(x_plot)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(x_plot, y_plot, label="Função objetivo", color="tab:blue")
    plt.scatter(population, objective(population), color="tab:orange", alpha=0.7, label="População final")
    plt.scatter([best_solution], [best_value], color="tab:red", s=80, label="Melhor solução")
    plt.title("Solução encontrada pelo Algoritmo Genético")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(range(1, len(fitness_history) + 1), fitness_history, marker="o", markersize=4)
    plt.title("Histórico do melhor fitness")
    plt.xlabel("Geração")
    plt.ylabel("Melhor fitness")
    plt.grid(True)

    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), "genetic_ga_result.png")
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"Gráfico salvo em: {output_path}")


def main() -> None:
    params = GAParams(
        population_size=20,
        generations=100,
        crossover_rate=0.85,
        mutation_rate=0.08,
        mutation_scale=0.03,
        tournament_size=4,
        elite_size=3,
        search_bounds=(-1.0, 1.0),
        random_seed=123,
    )

    population, fitness_history, best_solution, best_value = run_genetic_algorithm(params)

    print("\nMelhor solução encontrada:")
    print(f"x = {best_solution:.8f}")
    print(f"y = {best_value:.8f}")

    plot_results(params, population, fitness_history, best_solution, best_value)


if __name__ == "__main__":
    main()
