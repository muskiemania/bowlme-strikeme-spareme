

const getSuit = (card) => {

    // no card == error
    if (card === '') {
        return 'E';
    }

    // card part is second character
    const cardPart = card.charAt(1);

    // because suits are represented by special chars in the Card Font
    const xlate = {
        'C': ']',
        'D': '[',
        'H': '{',
        'S': '}'
    };

    return (cardPart in xlate) ? xlate[cardPart]: cardPart;
}

const getSuitName = (card) => {

    // no card == error
    if (card === '') {
        return 'E';
    }

    // card part is second character
    const cardPart = card.charAt(1);

    // because suits are represented by special chars in the Card Font
    const xlate = {
        'C': 'clubs',
        'D': 'diamonds',
        'H': 'hearts',
        'S': 'spades'
    };

    return (cardPart in xlate) ? xlate[cardPart]: cardPart;
}

export { getSuit, getSuitName };
