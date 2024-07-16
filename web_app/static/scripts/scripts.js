// JavaScript for web_app

// {Events.html} Load more events
document.addEventListener('DOMContentLoaded', function() {
  let offset = 8;

  document.querySelector('.load-more-button').addEventListener('click', function () {
    fetch(`/load-more-events?offset=${offset}`)
      .then(response => response.json())
      .then(data => {
        const eventsGrid = document.querySelector('.events-grid');
        data.events.forEach(event => {
          const eventItem = document.createElement('div');
          eventItem.classList.add('event-item');
          eventItem.innerHTML = `
                          <h3>${event.title}</h3>
                          <p><strong>Date:</strong> ${event.date}</p>
                          <p><strong>Time:</strong> ${event.time}</p>
                          <p><strong>Location:</strong> ${event.location}</p>
                          <p><strong>Description:</strong> ${event.description}</p>
                          <div class="event-buttons">
                              <a class="event-link-button" href="/events/${event.id}">More Info</a>
                              <a class="event-register-button" href="/register/${event.id}">Register</a>
                          </div>
                      `;
          eventsGrid.appendChild(eventItem);
        });
        offset += 8;
      })
      .catch(error => console.error('Error loading more events:', error));
  });
});


// {Forms} Toggle password visibility
document.addEventListener('DOMContentLoaded', function() {
  // Make togglePassword a global function
  window.togglePassword = function(inputId) {
      const input = document.getElementById(inputId);
      const button = input.nextElementSibling.nextElementSibling;
      const icon = button.querySelector('i');

      if (input.type === 'password') {
          input.type = 'text';
          icon.classList.remove('fa-eye');
          icon.classList.add('fa-eye-slash');
      } else {
          input.type = 'password';
          icon.classList.remove('fa-eye-slash');
          icon.classList.add('fa-eye');
      }
  };

  // You can add more form-related code here if needed
});