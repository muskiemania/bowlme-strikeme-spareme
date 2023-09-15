

const getCardinality = (card) => {

    // no card == error
    if (card === '') {
        return 'E';
    }

    // card part is first character
    const cardPart = card.charAt(0);

    // because 10 is represented by = in the Card Font
    const xlate = {'T': '='};

    if (['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K'].includes(cardPart)) {
        return (cardPart in xlate) ? xlate[cardPart] : cardPart;
    }

    return 'E';
}

export { getCardinality };
