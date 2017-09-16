export default function getSuit(card) {
    let cardPart = card.charAt(1);

    let xlate = {};
    xlate['clubs'] = ']';
    xlate['diamonds'] = '[';
    xlate['hearts'] = '{';
    xlate['spades'] = '}';

    let xlated = cardPart;
    if(cardPart in xlate) {
        xlated = xlate[cardPart];
    }

    return xlated;
}
