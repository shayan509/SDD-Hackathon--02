# Data Model: Public Todo MVP

## TodoItem Entity

### Fields
- **id**: Integer, Primary Key, Auto-generated
- **task**: String (Text), Required, Max length 500 characters
- **is_done**: Boolean, Default False

### Relationships
- No relationships with other entities (standalone entity)

### Validation Rules
- task field must not be empty (length > 0)
- task field must not exceed 500 characters
- is_done field must be boolean type

### State Transitions
- is_done transitions from False to True (when toggled complete)
- is_done transitions from True to False (when toggled incomplete)

### Indexes
- Primary index on id field
- No additional indexes required for MVP

### Constraints
- task field cannot be NULL
- is_done field cannot be NULL (defaults to False)