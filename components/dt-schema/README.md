# Decision Table Schema

This sample demonstrates generating Java wrappers from a decision table 
model (schema file) and using the wrappers to create and populate a 
StreamBase decision table. For simplicity, the content written to the 
decision table is hard-coded.

The following error is initially present when this project is loaded into
StreamBase Studio:

Execution response-xjc of goal org.jvnet.jaxb2.maven2:maven-jaxb2-plugin:
0.13.1: generate failed: org.xml.sax.SAXNotSupportedException: 
FEATURE_SECURE_PROCESSING: Cannot set the feature to false when security 
manager is present. 

To eliminate this error and generate the Java wrappers, run the dt-schema 
launch configuration included with this project:

    Run > Run Configurations... > Maven Build > dt-schema
    
and then refresh the project:

    Project Explorer > right-click dt-schema project > Refresh

Once the wrappers are generated, run CreateDecisionTable.java, which uses
the wrappers to write a sample decision table, sample.sbdt. This decision
table can be opened in Studio's Decision Table editor and loaded into
the Decision Table operator.  

* [Decision Table Schema](src/site/markdown/index.md)

_This is a Tibco approved sample_

---
Copyright (c) 2018-2019, TIBCO Software Inc.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.