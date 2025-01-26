#open prolog online compiler
#enter smiles(ram). after execute code
% Facts
graduating_status(ram).  % Ram is graduating

% Rules
graduating(X) :- graduating_status(X).  % If someone is graduating, they are graduating
happy(X) :- graduating(X).  % If someone is graduating, they are happy
smiles(X) :- happy(X).  % If someone is happy, they smile

% Query: Ask if Ram smiles
% To ask if Ram smiles, we query the smiles predicate
