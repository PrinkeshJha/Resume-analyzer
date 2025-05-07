
// DOM Elements
document.addEventListener('DOMContentLoaded', function() {
  // Theme Toggle
  const themeToggle = document.getElementById('theme-toggle');
  const themeIcon = themeToggle.querySelector('i');
  
  // Mobile Menu
  const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
  const navLinks = document.querySelector('.nav-links');
  
  // Resume Upload
  const uploadArea = document.getElementById('upload-area');
  const resumeFileInput = document.getElementById('resume-file');
  const uploadBtn = document.getElementById('upload-btn');
  const resultsSection = document.getElementById('results-section');
  const careerResults = document.getElementById('career-results');
  
  // Contact Form
  const contactForm = document.getElementById('contact-form');
  
  // Toast
  const toast = document.getElementById('toast');
  const toastMessage = document.getElementById('toast-message');
  
  // Theme Toggle Functionality
  themeToggle.addEventListener('click', function() {
    document.body.classList.toggle('dark-theme');
    document.body.classList.toggle('light-theme');
    
    // Update icon
    if (document.body.classList.contains('dark-theme')) {
      themeIcon.className = 'fas fa-sun';
      localStorage.setItem('theme', 'dark');
    } else {
      themeIcon.className = 'fas fa-moon';
      localStorage.setItem('theme', 'light');
    }
  });
  
  // Check for saved theme preference
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'dark') {
    document.body.classList.remove('light-theme');
    document.body.classList.add('dark-theme');
    themeIcon.className = 'fas fa-sun';
  }
  
  // Mobile Menu Toggle
  if (mobileMenuBtn) {
    mobileMenuBtn.addEventListener('click', function() {
      navLinks.classList.toggle('active');
      
      // Change hamburger to X
      const spans = this.querySelectorAll('span');
      if (navLinks.classList.contains('active')) {
        spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        spans[1].style.opacity = '0';
        spans[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
      } else {
        spans[0].style.transform = 'none';
        spans[1].style.opacity = '1';
        spans[2].style.transform = 'none';
      }
    });
  }
  
  // Resume Upload Functionality
  if (uploadArea && resumeFileInput) {
    // Handle drag and drop events
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
      uploadArea.addEventListener(eventName, preventDefaults, false);
    });
    
    function preventDefaults(e) {
      e.preventDefault();
      e.stopPropagation();
    }
    
    // Highlight drop area when item is dragged over
    ['dragenter', 'dragover'].forEach(eventName => {
      uploadArea.addEventListener(eventName, highlight, false);
    });
    
    ['dragleave', 'drop'].forEach(eventName => {
      uploadArea.addEventListener(eventName, unhighlight, false);
    });
    
    function highlight() {
      uploadArea.classList.add('active');
    }
    
    function unhighlight() {
      uploadArea.classList.remove('active');
    }
    
    // Handle dropped files
    uploadArea.addEventListener('drop', handleDrop, false);
    
    function handleDrop(e) {
      const dt = e.dataTransfer;
      const file = dt.files[0];
      
      if (file) {
        handleFile(file);
      }
    }
    
    // Handle file input selection
    uploadArea.addEventListener('click', () => {
      resumeFileInput.click();
    });
    
    resumeFileInput.addEventListener('change', function(e) {
      if (this.files && this.files[0]) {
        handleFile(this.files[0]);
      }
    });
    
    function handleFile(file) {
      // Check if file type is valid
      const validTypes = ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'text/plain'];
      if (!validTypes.includes(file.type)) {
        showToast('Please upload a PDF, DOCX, or TXT file.');
        return;
      }
      
      // Check if file size is less than 5MB
      if (file.size > 5 * 1024 * 1024) {
        showToast('File size should be less than 5MB.');
        return;
      }
      
      // Update UI to show selected file
      const fileName = file.name;
      const fileSize = (file.size / 1024).toFixed(2) + ' KB';
      uploadArea.innerHTML = `
        <i class="fas fa-file"></i>
        <p>${fileName}</p>
        <small>${fileSize}</small>
      `;
      
      // Enable upload button
      uploadBtn.disabled = false;
    }
    
    // Handle resume analysis
    uploadBtn.addEventListener('click', function() {
      // Show loading state
      this.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
      this.disabled = true;
      
      // Get the file
      const file = resumeFileInput.files[0];
      if (!file) {
        showToast('Please select a file first.');
        this.innerHTML = 'Analyze Resume';
        this.disabled = false;
        return;
      }
      
      // Create FormData and append the file
      const formData = new FormData();
      formData.append('resume', file);
      
      // Send request to Flask backend
      fetch('http://localhost:5000/api/analyze-resume', {
        method: 'POST',
        body: formData
      })
      .then(response => {
        if (!response.ok) {
          throw new Error('Server responded with an error: ' + response.status);
        }
        return response.json();
      })
      .then(data => {
        // Display the results
        displayResults(data.careerMatches);
        
        // Reset upload button
        uploadBtn.innerHTML = 'Analyze Resume';
        uploadBtn.disabled = false;
        
        // Show success message
        showToast('Resume analysis completed successfully!');
      })
      .catch(error => {
        console.error('Error:', error);
        
        // Reset upload button
        uploadBtn.innerHTML = 'Analyze Resume';
        uploadBtn.disabled = false;
        
        // Show error message
        showToast('An error occurred during analysis. Please try again.');
      });
    });
    
    function displayResults(results) {
      // Clear previous results
      careerResults.innerHTML = '';
      
      // Add career cards to the results section
      results.forEach(career => {
        const careerCard = document.createElement('div');
        careerCard.className = 'career-card';
        
        // Create skills list HTML
        let skillsHTML = '';
        career.skills.forEach(skill => {
          skillsHTML += `<span class="skill-tag">${skill}</span>`;
        });
        
        careerCard.innerHTML = `
          <h3>${career.title}</h3>
          <div class="match-score">Match Score: <span>${career.matchScore}%</span></div>
          <p>${career.description}</p>
          <div class="skills-match">
            <p>Key Matching Skills:</p>
            <div class="skills-list">
              ${skillsHTML}
            </div>
          </div>
        `;
        
        careerResults.appendChild(careerCard);
      });
      
      // Show results section
      resultsSection.style.display = 'block';
      
      // Scroll to results
      resultsSection.scrollIntoView({ behavior: 'smooth' });
    }
  }
  
  // Contact Form Submission
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();
      
      // Get form data
      const name = this.elements.name.value;
      const email = this.elements.email.value;
      const subject = this.elements.subject.value;
      const message = this.elements.message.value;
      
      // In a real application, you would send this data to a server
      console.log('Form submission:', { name, email, subject, message });
      
      // Reset form
      this.reset();
      
      // Show success message
      showToast('Your message has been sent. We\'ll get back to you soon!');
    });
  }
  
  // Toast notification function
  function showToast(message) {
    toastMessage.textContent = message;
    toast.classList.add('show');
    
    setTimeout(() => {
      toast.classList.remove('show');
    }, 5000);
  }
});
