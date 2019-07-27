Intro
=====

I recently met a program available for different architecture and OS version. 
Although one of them was including debugging symbols, the windows version obviously didn't come with it's pdb file.
As the code was big and everything was different (calling convention, opcode, registers ..),  I thought I could still use the binary strings from the other version as a way to quickly identify and navigate through the big function list.

wut ?
=====

The generateSig() function in the script will look for 1-1 relation between fonction strings by looking for unique strings with unique xrefs to a function. 

It will then create a simple sig file which can be loaded with loadSig() function
This might be a simple approach but I think it can generally came in handy for identifying libraries functions and is less complex to do than flair signature.

improvement
===========

As the function is identified, an obvious improvement would be to provide other debug symbols information (variable name, struct).
