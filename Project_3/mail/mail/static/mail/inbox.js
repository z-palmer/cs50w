document.addEventListener('DOMContentLoaded', function () {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#mailbox-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  document.querySelector('#compose-form').onsubmit = function () {

    // variablize form values to insert into table
    const recipients = document.querySelector('#compose-recipients').value;
    const subject = document.querySelector('#compose-subject').value;
    const body = document.querySelector('#compose-body').value;

    // fetch to insert to API
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
        recipients: recipients,
        subject: subject,
        body: body
      })
    })
      .then(response => response.json())
      .then(result => {
        console.log(result);
        load_mailbox('sent');
      });
  }
  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {

  // Show the mailbox and hide other views
  document.querySelector('#mailbox-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#mailbox-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  if (mailbox === 'inbox') {

    // load inbox
    fetch('/emails/inbox')
      .then(response => response.json())
      .then(emails => {
        console.log(emails);
        emails.forEach(element => {
          // create previews for each email in response
          const email = document.createElement('div');
          email.className = 'email-preview';
          email.id = element.id;
          email.innerHTML = `<h6><strong>From:</strong>  ${element.sender} 
          <strong>Subject:</strong>  ${element.subject} 
          <strong>Time:</strong>  ${element.timestamp}<h6>`;
          email.addEventListener('click', () => {
            email.style.backgroundColor = 'grey';
            load_email(email.id);
          });
          document.querySelector('#mailbox-view').append(email);
        });
      });
  }

  else if (mailbox === 'sent') {

    // load sent mail
    fetch('/emails/sent')
      .then(response => response.json())
      .then(emails => {
        console.log(emails);
      });
  }

  else if (mailbox === 'archive') {

    // load archive
    fetch('/emails/archive')
      .then(response => response.json())
      .then(emails => {
        console.log(emails);
      });
  }
}

function load_email(id) {

  document.querySelector('#mailbox-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  fetch(`/emails/${id}`)
    .then(response => response.json())
    .then(email => {
      console.log(email);
      const header = document.createElement('div');
      header.className = 'email-header';
      header.innerHTML = `<h5>From:</h5> ${email.sender}
      <h5>To:</h5> ${email.recipients}
      <h5>Subject:</h5> ${email.subject}
      <h5>Time:</h5> ${email.timestamp}`;
      const body = document.createElement('div');
      body.className = 'email-body';
      body.innerHTML = `<p>${email.body}</p>`

      document.querySelector('#email-view').append(header, body);
    });
}