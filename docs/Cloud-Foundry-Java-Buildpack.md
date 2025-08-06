Starting from version [v4.9](https://github.com/cloudfoundry/java-buildpack/releases/tag/v4.9) of the Cloud Foundry (CF) [Java Buildpack](https://github.com/cloudfoundry/java-buildpack), SapMachine can be used as a standard Java Runtime Environment. 
In order to use the SapMachine JRE, set the following environment variable for your Cloud Foundry application:

`cf set-env <app_name> JBP_CONFIG_COMPONENTS '{jres: ["JavaBuildpack::Jre::SapMachineJRE"]}' `

`cf restage <app_name>`

Alternatively, you can declare the environment variable in the application's manifest file:
```
  env:
      JBP_CONFIG_COMPONENTS: '{jres: ["JavaBuildpack::Jre::SapMachineJRE"]}'
```

or even specifying a concrete version, using the [version syntax](https://github.com/cloudfoundry/java-buildpack/blob/63545391234676b91642b7e0c5f946113ac8b3b4/docs/extending-repositories.md#version-syntax-and-ordering):
```
  env:
      JBP_CONFIG_COMPONENTS: '{jres: ["JavaBuildpack::Jre::SapMachineJRE"]}'
      JBP_CONFIG_SAP_MACHINE_JRE: '{ jre: { version: 21.+ } }'
```

For more detailed instructions pleases check out the CF [documentation](https://github.com/cloudfoundry/java-buildpack/blob/master/docs/jre-sap_machine_jre.md).

To profile your application, obtain a heap dump or a thread dump, you can use our [cf java plugin](https://github.com/SAP/cf-cli-java-plugin).
