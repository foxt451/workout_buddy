import * as dateFns from "https://esm.run/date-fns";

export class ChatUI {
    constructor(list) {
        this.list = list;
    }

    html = (username, userlink, msg, dateNormal) => `
    <li class="list-group-item">
        <a class="text-primary username" href="${userlink}">${_.escape(username)}</a>
        <br>
        <span class="message">${_.escape(msg)}</span>
        <div class="time text-muted">${dateFns.formatDistanceToNow(dateNormal)} ago</div>
    </li>
    `;

    addMessage(msgDoc, username, userlink) {
        this.list.innerHTML += this.html(username, userlink, msgDoc.message, msgDoc.created_at.toDate())
    }

    clear() {
        this.list.innerHTML = '';
    }
}