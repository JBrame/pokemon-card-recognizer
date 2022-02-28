from typing import List, Tuple

import numpy as np
from pokemontcgsdk import Card


def compute_basic_acc(preds: np.array, gt: np.array) -> [float, List[int]]:
    """
    Computes accuracy, excluding alternate art duplicates.

    :param preds: The predictions made for each card as list of card numbers(np.array[int])
    :param gt: The ground truth card number for each point (np.array[int])
    :return:
        acc: Computed accuracy
        incorrect: Vector of incorrect prediction indices
    """
    assert len(preds) == len(gt), 'preds and gt must have same size.'
    acc = np.sum(preds == gt) / len(gt)
    incorrect = np.where(preds != gt)[0]
    return acc, incorrect


def compute_acc_exclude_alt_art(preds: np.array, gt: np.array, cards_reference: List[Card]) -> Tuple[float, List[int]]:
    """
    Computes accuracy, excluding alternate art duplicates.

    :param preds: The predictions made for each card as list of card numbers(np.array[int])
    :param gt: The ground truth card number for each point (np.array[int])
    :param cards_reference: Cards reference for set
    :return:
        acc: Computed accuracy
    """
    assert len(preds) == len(gt), 'preds and gt must have same size.'
    num_correct = 0
    incorrect = np.full((len(preds), ), True, dtype=bool)
    for i, pred in enumerate(preds):
        if pred == gt[i]:
            incorrect[i] = False
            num_correct += 1
        else:
            if cards_reference[int(pred)].name == cards_reference[gt[i]].name:
                incorrect[i] = False
                num_correct += 1
    acc = num_correct / len(preds)
    incorrect = np.where(incorrect)[0]
    return acc, incorrect
