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
  document.querySelector('#emails-view').style.display = 'none';
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
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  if (mailbox === 'inbox') {

    // load inbox
    fetch('/emails/inbox')
      .then(response => response.json())
      .then(emails => {
        console.log(emails);
        emails.forEach(element => {
          const email = document.createElement('div');
          email.className = 'email-preview';
          email.innerHTML = `<h5><strong>From:</strong> ${element.sender} 
          <strong>Subject:</strong> ${element.subject} 
          <strong>Time:</strong> ${element.timestamp}<h5>`;
          document.querySelector('#emails-view').append(email);
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