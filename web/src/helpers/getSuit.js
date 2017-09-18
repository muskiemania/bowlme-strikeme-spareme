export function getSuit(card) {

    if(card === '') {
        return 'E';
    }
    
    let cardPart = card.charAt(1);

    let xlate = {};
    xlate['C'] = ']';
    xlate['D'] = '[';
    xlate['H'] = '{';
    xlate['S'] = '}';

    let xlated = cardPart;
    if(cardPart in xlate) {
        xlated = xlate[cardPart];
    }

    return xlated;
}
