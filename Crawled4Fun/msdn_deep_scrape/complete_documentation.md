# XNA Game Studio 3.1 - Complete Microcode Documentation

**Complete documentation scraped from MSDN Wayback Machine (Deep Crawl)**

**Scrape Date:** 2025-08-30 13:14:19
**Total Pages:** 21
**Total Words:** 11,533

## Content Overview

- **Main Pages:** 1
- **Section Pages:** 5
- **Instruction Pages:** 15

---

# PART I: MAIN DOCUMENTATION

## Microcode (xvs_3_0, xps_3_0)

**Source:** http://msdn.microsoft.com:80/en-us/library/bb313877.aspx
**Word Count:** 260

XNA Game Studio 3.1
Microcode (xvs_3_0, xps_3_0)
This section describes inline microcode shaders for Xbox 360. These shaders may be written in as inline microcode and compiled with the XNA Framework Content Pipeline. 
Microcode assembly language is the native shader assembly language of Xbox 360. It is a different language than the DX token assembly language used by Direct3D for Microsoft Windows.
You can write inline microcode assembly within an HLSL shader using the **asm** directive.
Microcode assembly language supports a superset of the ps_3_0 and vs_3_0 specifications defined by Direct3D 9.0 for Windows. It does not support earlier Direct3D vertex and pixel shader specifications. The microcode assembly vertex shader specification is defined as xvs_3_0, while the microcode assembly pixel shader specification is defined as xps_3_0.
# In This Section 

[Inline Microcode Assembly](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313871.aspx)
    Describes how to use inline assembly. Explains its limitations. 

[Vertex Fetching](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313874.aspx)
    Describes vertex fetching. Explains how to implement an alternative to **SetSource**. 

[Texture Fetching with extra Xbox 360-specific Parameters](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313873.aspx)
    Describes texture fetching. Explains how to take advantage of extra parameters, such as texel offsets. 

[Source Register Swizzling](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313962.aspx)
    Describes source register swizzling. 

[Microcode Instructions](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313961.aspx)
    Discusses the various instructions that can be used in microcode programs.
  
[Inline Microcode Assembly in HLSL](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313871.aspx)  
[Vertex Fetching in HLSL (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313874.aspx)  
[Texture Fetching in HLSL (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313873.aspx)  
[Swizzling (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313962.aspx)  
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313961.aspx)
* * *
  
[MSDN Library](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/aa468128.aspx)  
[XNA Game Studio 3.1](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313877.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20100423054747im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

## Inline Microcode Assembly in HLSL

**Source:** http://msdn.microsoft.com/en-us/library/bb313871.aspx
**Word Count:** 397

XNA Game Studio 3.1
Inline Microcode Assembly in HLSL
The **asm** keyword allows Xbox 360 GPU microcode to be inserted (inline) into HLSL functions, as shown here. 
```
float4 FetchPosition( int i )
{
  float4 vertexPos;
  asm {
    vfetch vertexPos, i, position
  };
  return vertexPos;
}  
```

The inline microcode starts with **asm{** , followed by one or more microcode statements. It ends with **};**. The trailing semicolon at the end of the microcode block is always required.
The **asm** block does not contain a target such as **xvs_3_0** or **xps_3_0**. This allows the same routine to be called from both vertex shaders and pixel shaders. On Xbox 360, the **asm** block supports only [Xbox 360 microcode](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/bb313877.aspx).
# Sequencer Statements
  * No control flow statements are allowed. Instead, use one or more **asm** blocks with HLSL control flow.
```
for ( int i = 0; i < 2; i++ )
{
  asm {
  // one or more microcode statements
  };
};        
```



# Registers and Variables
  * The microcode must use HLSL local or global variable names. The **asm** microcode block cannot use any registers.
  * Only simple HLSL variables are allowed within the microcode—no structures or arrays. These variables can be swizzled.
  * HLSL variables can be used as the "value" part of a name-value pair in addition to being used as source and destination arguments.
```
float4 fetchS( sampler2D s, float2 uv, float offsetX )
{
  float4 result;
  asm {
    tfetch2D result, uv, s, OffsetX = offsetX
  };
  return result;
}        
```



# HLSL Variable Binding in Microcode
If a symbol is used as a microcode source, destination, or value argument, the symbol's meaning is determined as follows.
  1. If the symbol is a variable in the lexically enclosed HLSL environment, then that variable is used.
  2. If the symbol appears as a "value" argument, and the symbol matches one of the existing GPU microcode enumerated types, then that enumerated value is used.


See Also
* * *
#### Concepts
[Vertex Fetching in HLSL (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/bb313874.aspx)  
[Texture Fetching in HLSL (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/bb313873.aspx)  
[Swizzling (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/bb313962.aspx)  

#### Reference
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/bb313961.aspx)  

* * *
  
[MSDN Library](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/aa468128.aspx)  
[XNA Game Studio 3.1](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  
[Inline Microcode Assembly in HLSL](https://web.archive.org/web/20100423055133/http://msdn.microsoft.com/en-us/library/bb313871.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20100423055133im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

## Vertex Fetching in HLSL (xvs_3_0, xps_3_0)

**Source:** http://msdn.microsoft.com/en-us/library/bb313874.aspx
**Word Count:** 268

XNA Game Studio 3.1
Vertex Fetching in HLSL (xvs_3_0, xps_3_0)
Vertex fetching in HLSL is implemented by using a combination of the INDEX input semantic and an **asm** block that uses a [vfetch](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/bb313960.aspx) instruction. 
The following HLSL code shows how vertex fetching can be used to implement an alternative to [SetFrequency](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/microsoft.xna.framework.graphics.vertexstream.setfrequency.aspx). Note that the INDEX input semantic is associated with a parameter of type **int**. 
```
    float instanceSize : register( c0 ); // Set by application code.
    
    struct vsout {
      float4 p : POSITION;
      float4 c : COLOR;
    };
    
    float4 fetchPosition( int index )
    {
      float4 pos;
      asm {
        vfetch pos, index, position
      };
      return pos;
    }
    
    float4 fetchDelta( int index )
    {
      float4 pos;
      asm {
        vfetch pos, index, position1
      };
      return pos;
    }

    float4 fetchColor( int index )
    {
      float4 color;
      asm {
        vfetch color, index, color
      };
      return color;
    }
    
    vsout main( int i : INDEX )
    {
      vsout output;
      
      // Add 0.5 before dividing to avoid rounding errors.
      int outerIndex = (i + 0.5) / instanceSize;
      
      int innerIndex = i - outerIndex * instanceSize;
      output.p = fetchPosition( innerIndex ) + fetchDelta( outerIndex );
      output.c = fetchColor( outerIndex );
      return output;
    }
  
```

See Also
* * *
#### Concepts
[Inline Microcode Assembly in HLSL](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/bb313871.aspx)  
[Texture Fetching in HLSL (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/bb313873.aspx)  
[Swizzling (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/bb313962.aspx)  

#### Reference
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/bb313961.aspx)  

* * *
  
[MSDN Library](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/aa468128.aspx)  
[XNA Game Studio 3.1](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  
[Vertex Fetching in HLSL (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423061946/http://msdn.microsoft.com/en-us/library/bb313874.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20100423061946im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

## Texture Fetching in HLSL (xvs_3_0, xps_3_0)

**Source:** http://msdn.microsoft.com/en-us/library/bb313873.aspx
**Word Count:** 248

XNA Game Studio 3.1
Texture Fetching in HLSL (xvs_3_0, xps_3_0)
Inline microcode assembly can be used to access the [extra parameters](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/bb313958.aspx) that are available when fetching texures. This is useful primarily for the **OffsetX** , **OffsetY** , and **OffsetZ** parameters. 
The following code demonstrates texture fetching in HLSL.
```
    struct vsout {
      float4 p : POSITION;
      float4 uv : TEXCOORD;
    };
    
    struct psin {
      float4 uv : TEXCOORD;
    };
    
    vsout TFetchVS( vsout input )
    {
      return input;
    }
    
    sampler2D s : register( s0 );
    
    float4 tex2DOffset( sampler2D ss, float2 uv, float2 offset )
    {
      float4 result;
      float offsetX = offset.x;
      float offsetY = offset.y;
     
      asm {
        tfetch2D result, uv, ss, OffsetX = offsetX,
        OffsetY = offsetY
      };
      
      return result;
    }

    float4 TFetchPS( psin input ) : COLOR
    {
      float4 sum = 0;
     
      for( int i = 0; i < 3; i++ )
      {
        for( int j = 0; j < 3; j++ )
        {
          sum += tex2DOffset( s, input.uv, float2( i - 1, j - 1 ) );
        }
      }
      
      return sum / 9.0;
    }
  
```

See Also
* * *
#### Concepts
[Inline Microcode Assembly in HLSL](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/bb313871.aspx)  
[Vertex Fetching in HLSL (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/bb313874.aspx)  
[Swizzling (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/bb313962.aspx)  

#### Reference
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/bb313961.aspx)  

* * *
  
[MSDN Library](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/aa468128.aspx)  
[XNA Game Studio 3.1](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  
[Texture Fetching in HLSL (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423063105/http://msdn.microsoft.com/en-us/library/bb313873.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20100423063105im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

## Swizzling (xvs_3_0, xps_3_0)

**Source:** http://msdn.microsoft.com/en-us/library/bb313962.aspx
**Word Count:** 784

XNA Game Studio 3.1
Swizzling (xvs_3_0, xps_3_0)
Swizzling is a way of specifying which inputs go to what channels and only applies to input registers. There are four different types of swizzling, based on the instruction type.
  * [vfetch Instructions](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313962.aspx#vfetch)
  * [tfetch Instructions](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313962.aspx#tfetch)
  * [Vector ALU Instructions](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313962.aspx#vector)
  * [Scalar ALU Instructions](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313962.aspx#scalar)


# vfetch Instructions
The one-component swizzle for **vfetch** instructions is always of the following form.
```
_src_.{x|y|z|w}
```

# tfetch Instructions
There are four **tfetch** instructions. The swizzling for these instructions is used to indicate the components of the source register to use for the texture lookup. Each instruction is of the following form.
```
tfetch _dest_, _src_, _fetchConst_
```

## tfetch1D
The [tfetch1D](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313956.aspx) instruction performs a 1D texture lookup. The _src_ register must have a one-component swizzle. For example, _src_ might be r4.x. The swizzle (".x" in this case) indicates that the texture coordinate comes from the x-component of the r4 register.
The one-component swizzle for the [tfetch1D](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313956.aspx) instruction is always of the following form.
```
_src_.{x|y|z|w}
```

## tfetch2D
The [tfetch2D](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313957.aspx) instruction performs a 2D texture lookup. The _src_ register must have a two-component swizzle. For example, _src_ might be r4.wx. The swizzle (".wx" in this case) indicates that the w- and x-components are used to lookup the U and V texture coordinates, respectively.
The two-component swizzle for the [tfetch2D](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313957.aspx) instruction is always of the following form.
```
_src_.{x|y|z|w}{x|y|z|w}
```

## tfetch3D and tfetchCube
The [tfetch3D](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313958.aspx) instruction performs a 3D texture lookup. The [tfetchCube](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313959.aspx) instruction performs a cube texture lookup. The _src_ register must have a three-component swizzle. For example, _src_ might be r4.wxz. The swizzle (".wxz" in this case) indicates that the w-, x- and z-components are used to lookup the u, v and w texture coordinates, respectively.
The three-component swizzle for these two instructions is always of the following form.
```
_src_.{x|y|z|w}{x|y|z|w}{x|y|z|w}
```

# Vector ALU Instructions
Every [vector ALU instruction](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313916.aspx) may make use of an optional four-component swizzle. This swizzle allows individual components of the source register to temporarily take on the value of any of the four components of the same register, before that register is read for computation. The contents of the source register are not modified by the swizzle.
The four-component swizzle for the vector ALU instructions is always of the following form.
```
_src_[.{x|y|z|w}[x|y|z|w][x|y|z|w][x|y|z|w]]
```

The first optional block specifies the x-component, the second optional block specifies the y-component, and so on. For example, the .zxxy swizzle means:
  * The x-component will temporarily take on the value of the z-component.
  * The y-component will temporarily take on the value of the x-component.
  * The z-component will temporarily take on the value of the x-component.
  * The w-component will temporarily take on the value of the y-component.


Components can appear in any order. If fewer than four components are specified, the last component is repeated. For example, .xy is the same as .xyyy, .wzx is the same as .wzxx, and .z is the same as .zzzz. If no components are specified, no swizzling occurs. No swizzling is the same as .xyzw.
# Scalar ALU Instructions
Every [scalar ALU instruction](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313879.aspx) requires either a one- or two-component swizzle that indicates the components to use for the scalar operation. Almost all scalar ALU instructions operate on a single component of the source register. These scalar instructions make use of a one-component swizzle. Consider the following example.
```
cos r4, r3.y
```

The ".y" swizzle on the source register tells the scalar instruction to use compute the cosine of the y-component of r3.
The one-component swizzle for the scalar ALU instructions is always of the following form.
```
_src_.{x|y|z|w}
```

There are six scalar ALU instructions that operate on two components of their source register.
  * [adds](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313880.aspx)
  * [maxs](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313891.aspx)
  * [mins](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313892.aspx)
  * [muls](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313896.aspx)
  * [muls_prev2](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313898.aspx)
  * [subs](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313913.aspx)


These six instructions require a two-component swizzle that indicates the components to use. Consider the following example.
```
subs r4, r3.zx
```

The ".zx" swizzle on the source register tells the scalar instruction to compute the difference of r3.z and r3.x.
The two-component swizzle for the scalar ALU instructions is always of the following form.
```
_src_.{x|y|z|w}{x|y|z|w}
```

The first mandatory component indicates the first operand for the instruction. The second mandatory component indicates the second operand for the instruction.
See Also
* * *
#### Concepts
[Inline Microcode Assembly in HLSL](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313871.aspx)  
[Vertex Fetching in HLSL (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313874.aspx)  
[Texture Fetching in HLSL (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313873.aspx)  

#### Reference
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313961.aspx)  

* * *
  
[MSDN Library](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/aa468128.aspx)  
[XNA Game Studio 3.1](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  
[Swizzling (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100429090724/http://msdn.microsoft.com/en-us/library/bb313962.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20100429090724im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

## Microcode Instructions (xvs_3_0, xps_3_0)

**Source:** http://msdn.microsoft.com/en-us/library/bb313961.aspx
**Word Count:** 125

XNA Game Studio 3.1
Microcode Instructions (xvs_3_0, xps_3_0)
This section discusses the various instructions that can be used in microcode programs. 
# In This Section 

[ALU Instructions](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313878.aspx) 
    Documentation for the ALU vector and scalar instructions. 

[Fetch Instructions](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313942.aspx) 
    Documentation for the instructions that fetch vertex and texture data.
See Also
* * *
#### Concepts
[Inline Microcode Assembly in HLSL](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313871.aspx)  
[Vertex Fetching in HLSL (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313874.aspx)  
[Texture Fetching in HLSL (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313873.aspx)  
[Swizzling (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313962.aspx)  

  
[ALU Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313878.aspx)  
[Fetch Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313942.aspx)
* * *
  
[MSDN Library](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/aa468128.aspx)  
[XNA Game Studio 3.1](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313961.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20100423054747im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

# PART II: INSTRUCTION REFERENCE

## Fetch Instructions (xvs_3_0, xps_3_0)

**Source:** http%3A//msdn.microsoft.com/en-us/library/bb313942.aspx
**Word Count:** 418

XNA Game Studio 3.1
Fetch Instructions (xvs_3_0, xps_3_0)
Provides microcode fetch instructions. 
Instruction | Description  
---|---  
[ getBCF1D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313943.aspx) |  Gets the fraction of border color that would be blended into the texture data (retrieved using a 1D-texture fetch) at the specified coordinates.  
[ getBCF2D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313944.aspx) |  Gets the fraction of border color that would be blended into the texture data (retrieved using a 2D-texture fetch) at the specified coordinates.  
[ getBCF3D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313945.aspx) |  Gets the fraction of border color that would be blended into the texture data (retrieved using a 3D-texture fetch) at the specified coordinates.  
[ getBCFCube](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313946.aspx) |  Gets the fraction of border color that would be blended into the texture data (retrieved using a cube-texture fetch) at the specified coordinates.  
[ getCompTexLOD1D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313947.aspx) |  For 1D textures, gets the LOD for all of the pixels in the quad at the specified coordinates.  
[ getCompTexLOD2D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313948.aspx) |  For 2D textures, gets the LOD for all of the pixels in the quad at the specified coordinates.  
[ getCompTexLOD3D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313949.aspx) |  For 3D textures, gets the LOD for all of the pixels in the quad at the specified coordinates.  
[ getCompTexLODCube](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313950.aspx) |  For cube textures, gets the LOD for all of the pixels in the quad at the specified coordinates.  
[ getWeights1D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313951.aspx) |  Gets the weights used in a bilinear fetch from a 1D texture.  
[ getWeights2D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313952.aspx) |  Gets the weights used in a bilinear fetch from 2D textures.  
[ getWeights3D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313953.aspx) |  Gets the weights used in a bilinear fetch from 3D textures.  
[ getWeightsCube](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313954.aspx) |  Gets the weights used in a bilinear fetch from cube textures.  
[ setTexLOD](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313955.aspx) |  Sets the level of detail.  
[ tfetch1D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313956.aspx) |  Fetches sample data from a 1D texture.  
[ tfetch2D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313957.aspx) |  Fetches sample data from a 2D texture.  
[ tfetch3D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313958.aspx) |  Fetches sample data from a 3D texture.  
[ tfetchCube](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313959.aspx) |  Fetches sample data from a cube texture.  
[ vfetch](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313960.aspx) |  Fetches data from a vertex buffer using a semantic.  
  
[getBCF1D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313943.aspx)  
[getBCF2D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313944.aspx)  
[getBCF3D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313945.aspx)  
[getBCFCube (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313946.aspx)  
[getCompTexLOD1D (xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313947.aspx)  
[getCompTexLOD2D (xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313948.aspx)  
[getCompTexLOD3D (xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313949.aspx)  
[getCompTexLODCube (xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313950.aspx)  
[getWeights1D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313951.aspx)  
[getWeights2D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313952.aspx)  
[getWeights3D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313953.aspx)  
[getWeightsCube (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313954.aspx)  
[setTexLOD (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313955.aspx)  
[tfetch1D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313956.aspx)  
[tfetch2D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313957.aspx)  
[tfetch3D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313958.aspx)  
[tfetchCube (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313959.aspx)  
[vfetch (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313960.aspx)
* * *
  
[MSDN Library](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/aa139594.aspx)  
[XNA Game Studio 3.1](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313961.aspx)  
[Fetch Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313942.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20090918114559im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

## Wayback Machine

**Source:** http://msdn.microsoft.com/en-us/library/bb313913.aspx
**Word Count:** 756

[Ask the publishers](https://change.org/LetReadersRead) to restore access to 500,000+ books.
Hamburger icon An icon used to represent a menu that can be toggled by interacting with this icon.
[ Internet Archive logo A line drawing of the Internet Archive headquarters building façade. ](https://archive.org/ "Go home")
[ Web icon An illustration of a computer application window Wayback Machine ](https://web.archive.org "Expand web menu") [ Texts icon An illustration of an open book.  Texts ](https://archive.org/details/texts "Expand texts menu") [ Video icon An illustration of two cells of a film strip. Video ](https://archive.org/details/movies "Expand video menu") [ Audio icon An illustration of an audio speaker.  Audio ](https://archive.org/details/audio "Expand audio menu") [ Software icon An illustration of a 3.5" floppy disk. Software ](https://archive.org/details/software "Expand software menu") [ Images icon An illustration of two photographs.  Images ](https://archive.org/details/image "Expand images menu") [ Donate icon An illustration of a heart shape  Donate ](https://archive.org/donate/ "Expand donate menu") [ Ellipses icon An illustration of text ellipses.  More ](https://archive.org/about/ "Expand more menu")
[ Donate icon An illustration of a heart shape "Donate to the archive" ](https://archive.org/donate/?origin=iawww-mbhrt)
User icon An illustration of a person's head and chest.  [Sign up](https://archive.org/account/signup) | [Log in](https://archive.org/account/login)
[ Upload icon An illustration of a horizontal line over an up pointing arrow. Upload ](https://archive.org/create) Search icon An illustration of a magnifying glass.
Search icon An illustration of a magnifying glass.
###  Internet Archive Audio
[![](https://archive.org/services/img/etree)Live Music Archive](https://archive.org/details/etree) [![](https://archive.org/services/img/librivoxaudio)Librivox Free Audio](https://archive.org/details/librivoxaudio)
#### Featured
  * [All Audio](https://archive.org/details/audio)
  * [Grateful Dead](https://archive.org/details/GratefulDead)
  * [Netlabels](https://archive.org/details/netlabels)
  * [Old Time Radio](https://archive.org/details/oldtimeradio)
  * [78 RPMs and Cylinder Recordings](https://archive.org/details/78rpm)


#### Top
  * [Audio Books & Poetry](https://archive.org/details/audio_bookspoetry)
  * [Computers, Technology and Science](https://archive.org/details/audio_tech)
  * [Music, Arts & Culture](https://archive.org/details/audio_music)
  * [News & Public Affairs](https://archive.org/details/audio_news)
  * [Spirituality & Religion](https://archive.org/details/audio_religion)
  * [Podcasts](https://archive.org/details/podcasts)
  * [Radio News Archive](https://archive.org/details/radio)


###  Images
[![](https://archive.org/services/img/metropolitanmuseumofart-gallery)Metropolitan Museum](https://archive.org/details/metropolitanmuseumofart-gallery) [![](https://archive.org/services/img/clevelandart)Cleveland Museum of Art](https://archive.org/details/clevelandart)
#### Featured
  * [All Images](https://archive.org/details/image)
  * [Flickr Commons](https://archive.org/details/flickrcommons)
  * [Occupy Wall Street Flickr](https://archive.org/details/flickr-ows)
  * [Cover Art](https://archive.org/details/coverartarchive)
  * [USGS Maps](https://archive.org/details/maps_usgs)


#### Top
  * [NASA Images](https://archive.org/details/nasa)
  * [Solar System Collection](https://archive.org/details/solarsystemcollection)
  * [Ames Research Center](https://archive.org/details/amesresearchcenterimagelibrary)


###  Software
[![](https://archive.org/services/img/internetarcade)Internet Arcade](https://archive.org/details/internetarcade) [![](https://archive.org/services/img/consolelivingroom)Console Living Room](https://archive.org/details/consolelivingroom)
#### Featured
  * [All Software](https://archive.org/details/software)
  * [Old School Emulation](https://archive.org/details/tosec)
  * [MS-DOS Games](https://archive.org/details/softwarelibrary_msdos_games)
  * [Historical Software](https://archive.org/details/historicalsoftware)
  * [Classic PC Games](https://archive.org/details/classicpcgames)
  * [Software Library](https://archive.org/details/softwarelibrary)


#### Top
  * [Kodi Archive and Support File](https://archive.org/details/kodi_archive)
  * [Vintage Software](https://archive.org/details/vintagesoftware)
  * [APK](https://archive.org/details/apkarchive)
  * [MS-DOS](https://archive.org/details/softwarelibrary_msdos)
  * [CD-ROM Software](https://archive.org/details/cd-roms)
  * [CD-ROM Software Library](https://archive.org/details/cdromsoftware)
  * [Software Sites](https://archive.org/details/softwaresites)
  * [Tucows Software Library](https://archive.org/details/tucows)
  * [Shareware CD-ROMs](https://archive.org/details/cdbbsarchive)
  * [Software Capsules Compilation](https://archive.org/details/softwarecapsules)
  * [CD-ROM Images](https://archive.org/details/cdromimages)
  * [ZX Spectrum](https://archive.org/details/softwarelibrary_zx_spectrum)
  * [DOOM Level CD](https://archive.org/details/doom-cds)


###  Texts
[![](https://archive.org/images/widgetOL.png)Open Library](https://openlibrary.org/) [![](https://archive.org/services/img/americana)American Libraries](https://archive.org/details/americana)
#### Featured
  * [All Texts](https://archive.org/details/texts)
  * [Smithsonian Libraries](https://archive.org/details/smithsonian)
  * [FEDLINK (US)](https://archive.org/details/fedlink)
  * [Genealogy](https://archive.org/details/genealogy)
  * [Lincoln Collection](https://archive.org/details/lincolncollection)


#### Top
  * [American Libraries](https://archive.org/details/americana)
  * [Canadian Libraries](https://archive.org/details/toronto)
  * [Universal Library](https://archive.org/details/universallibrary)
  * [Project Gutenberg](https://archive.org/details/gutenberg)
  * [Children's Library](https://archive.org/details/iacl)
  * [Biodiversity Heritage Library](https://archive.org/details/biodiversity)
  * [Books by Language](https://archive.org/details/booksbylanguage)
  * [Additional Collections](https://archive.org/details/additional_collections)


###  Video
[![](https://archive.org/services/img/tv)TV News](https://archive.org/details/tv) [![](https://archive.org/services/img/911)Understanding 9/11](https://archive.org/details/911)
#### Featured
  * [All Video](https://archive.org/details/movies)
  * [Prelinger Archives](https://archive.org/details/prelinger)
  * [Democracy Now!](https://archive.org/details/democracy_now_vid)
  * [Occupy Wall Street](https://archive.org/details/occupywallstreet)
  * [TV NSA Clip Library](https://archive.org/details/nsa)


#### Top
  * [Animation & Cartoons](https://archive.org/details/animationandcartoons)
  * [Arts & Music](https://archive.org/details/artsandmusicvideos)
  * [Computers & Technology](https://archive.org/details/computersandtechvideos)
  * [Cultural & Academic Films](https://archive.org/details/culturalandacademicfilms)
  * [Ephemeral Films](https://archive.org/details/ephemera)
  * [Movies](https://archive.org/details/moviesandfilms)
  * [News & Public Affairs](https://archive.org/details/newsandpublicaffairs)
  * [Spirituality & Religion](https://archive.org/details/spiritualityandreligion)
  * [Sports Videos](https://archive.org/details/sports)
  * [Television](https://archive.org/details/television)
  * [Videogame Videos](https://archive.org/details/gamevideos)
  * [Vlogs](https://archive.org/details/vlogs)
  * [Youth Media](https://archive.org/details/youth_media)


Search the history of over __WB_PAGES_ARCHIVED__ [web pages](https://blog.archive.org/2016/10/23/defining-web-pages-web-sites-and-web-captures/) on the Internet. 
[ ](https://web.archive.org) Search the Wayback Machine
Search icon An illustration of a magnifying glass.
#### Mobile Apps
  * [Wayback Machine (iOS)](https://apps.apple.com/us/app/wayback-machine/id1201888313)
  * [Wayback Machine (Android)](https://play.google.com/store/apps/details?id=com.archive.waybackmachine&hl=en_US)


#### Browser Extensions
  * [Chrome](https://chrome.google.com/webstore/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak)
  * [Firefox](https://addons.mozilla.org/en-US/firefox/addon/wayback-machine_new/)
  * [Safari](https://apps.apple.com/us/app/wayback-machine/id1472432422?mt=12)
  * [Edge](https://microsoftedge.microsoft.com/addons/detail/wayback-machine/kjmickeoogghaimmomagaghnogelpcpn?hl=en-US)


#### Archive-It Subscription
  * [Explore the Collections](https://www.archive-it.org/explore)
  * [Learn More](https://www.archive-it.org/blog/learn-more/)
  * [Build Collections](https://www.archive-it.org/contact-us)


### Save Page Now
Capture a web page as it appears now for use as a trusted citation in the future.
Please enter a valid web address
  * [About](https://archive.org/about/)
  * [Blog](https://blog.archive.org)
  * [Projects](https://archive.org/projects/)
  * [Help](https://archive.org/about/faqs.php)
  * [Donate](https://archive.org/donate?origin=iawww-TopNavDonateButton)
  * [Contact](https://archive.org/about/contact)
  * [Jobs](https://archive.org/about/jobs)
  * [Volunteer](https://archive.org/about/volunteer-positions)
  * [People](https://archive.org/about/bios)


  * [ Sign up for free  ](https://archive.org/account/signup)
  * [ Log in  ](https://archive.org/account/login)


Search metadata  Search text contents  Search TV news captions  Search radio transcripts  Search archived web sites  [Advanced Search](https://archive.org/advancedsearch.php)
  * [About](https://archive.org/about/)
  * [Blog](https://blog.archive.org)
  * [Projects](https://archive.org/projects/)
  * [Help](https://archive.org/about/faqs.php)
  * [Donate Donate icon An illustration of a heart shape ](https://archive.org/donate?origin=iawww-TopNavDonateButton)
  * [Contact](https://archive.org/about/contact)
  * [Jobs](https://archive.org/about/jobs)
  * [Volunteer](https://archive.org/about/volunteer-positions)
  * [People](https://archive.org/about/bios)


[DONATE](http://archive.org/donate/?origin=wbwww-CalndrDonateButton)
[](https://web.archive.org/)
Latest Show All
## Hrm.
The Wayback Machine has not archived that URL.
Click here to search for all archived pages under [http://msdn.microsoft.com/en-us/library/](https://web.archive.org/web/*/http://msdn.microsoft.com/en-us/library/*). 
The Wayback Machine is an initiative of the [Internet Archive](https://archive.org/), a 501(c)(3) non-profit, building a digital library of Internet sites and other cultural artifacts in digital form.   
Other [projects](https://archive.org/projects/) include [Open Library](https://openlibrary.org/) & [archive-it.org](https://archive-it.org). 
Your use of the Wayback Machine is subject to the Internet Archive's [Terms of Use](https://archive.org/about/terms.php). 


---

## Removed Content

**Source:** http%3A//msdn.microsoft.com/en-us/library/bb313892.aspx
**Word Count:** 241

[Home](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/default.aspx "Home") [Library](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/default.aspx "Library") [Learn](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/bb188199.aspx "Learn") [Downloads](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/aa570309.aspx "Downloads") [Support](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/hh361695.aspx "Support") [Community](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/aa497440.aspx "Community") |  [Sign in ](https://web.archive.org/web/20120423040211/https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=11&ct=1335153731&rver=6.0.5276.0&wp=MCLBI&wlcxt=msdn%24msdn%24msdn&wreply=http%3a%2f%2fmsdn.microsoft.com%2fen-us%2flibrary%2fbb313892.aspx&lc=1033&id=254354&mkt=en-US "Sign in") | [United States - English ](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/preferences/locale/?returnurl=%252fen-us%252flibrary%252fbb313892.aspx "United States - English") | [![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/preferences/experience/?returnurl=%252fen-us%252flibrary%252fbb313892.aspx "Preferences") | [![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/bb313892\(d=printer\).aspx "Print/Export") [![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)](javascript:void\(0\); "Print/Export")  
---|---  
|   
---|---  
![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[MSDN Library](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/ms123401.aspx "MSDN Library")
![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Design Tools](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/cc295789.aspx "Design Tools")
![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Development Tools and Languages](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/aa187916.aspx "Development Tools and Languages")
![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Mobile and Embedded Development](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/ms376734.aspx "Mobile and Embedded Development")
![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[.NET Development](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/ff361664\(v=vs.110\).aspx ".NET Development")
![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Office Development](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/bb726434\(v=office.12\).aspx "Office Development")
![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Online Services](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/ee702802.aspx "Online Services")
![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Open Specifications](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/dd208104\(v=prot.10\).aspx "Open Specifications")
![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[patterns & practices](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/ff921345.aspx "patterns & practices")
![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Servers and Enterprise Development](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/aa155072.aspx "Servers and Enterprise Development")
![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Speech Technologies](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/hh323806.aspx "Speech Technologies")
![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Web Development](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/aa155073.aspx "Web Development")
![](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Windows Development](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/ee663300\(v=vs.85\).aspx "Windows Development")
![Separator](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Global/Content/clear.gif)
[ ![Expand](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png) ![Minimize](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png) ](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/bb313892.aspx)
[ ![MSDN](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png) ](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/default.aspx)
This topic has not yet been rated [- Rate this topic](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/en-us/library/bb313892.aspx#feedback "Rate this topic")
# Removed Content
This content has been removed, but may be available in the product documentation installed on your computer.
Did you find this helpful? Yes No
Not accurate
Not enough depth
Need more code examples
Tell us more...
(1500 characters remaining)
© 2012 Microsoft. All rights reserved.
[Terms of Use](https://web.archive.org/web/20120423040211/http://msdn.microsoft.com/cc300389.aspx) |  [Trademarks](https://web.archive.org/web/20120423040211/http://www.microsoft.com/library/toolbar/3.0/trademarks/en-us.mspx) |  [Privacy Statement](https://web.archive.org/web/20120423040211/http://www.microsoft.com/info/privacy.mspx) |  Site Feedback [ Site Feedback  ![Site Feedback](https://web.archive.org/web/20120423040211im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png) ](https://web.archive.org/web/20120423040211/http://social.msdn.microsoft.com/Forums/en-US/libraryfeedback/threads "Site Feedback")
Site Feedback
[x](javascript:;)
Tell us about your experience... 
Did the page load quickly? 
Yes No
Do you like the page design? 
Yes No
Tell us more 
Enter description here.


---

## Wayback Machine

**Source:** http://msdn.microsoft.com/en-us/library/bb313898.aspx
**Word Count:** 756

[Ask the publishers](https://change.org/LetReadersRead) to restore access to 500,000+ books.
Hamburger icon An icon used to represent a menu that can be toggled by interacting with this icon.
[ Internet Archive logo A line drawing of the Internet Archive headquarters building façade. ](https://archive.org/ "Go home")
[ Web icon An illustration of a computer application window Wayback Machine ](https://web.archive.org "Expand web menu") [ Texts icon An illustration of an open book.  Texts ](https://archive.org/details/texts "Expand texts menu") [ Video icon An illustration of two cells of a film strip. Video ](https://archive.org/details/movies "Expand video menu") [ Audio icon An illustration of an audio speaker.  Audio ](https://archive.org/details/audio "Expand audio menu") [ Software icon An illustration of a 3.5" floppy disk. Software ](https://archive.org/details/software "Expand software menu") [ Images icon An illustration of two photographs.  Images ](https://archive.org/details/image "Expand images menu") [ Donate icon An illustration of a heart shape  Donate ](https://archive.org/donate/ "Expand donate menu") [ Ellipses icon An illustration of text ellipses.  More ](https://archive.org/about/ "Expand more menu")
[ Donate icon An illustration of a heart shape "Donate to the archive" ](https://archive.org/donate/?origin=iawww-mbhrt)
User icon An illustration of a person's head and chest.  [Sign up](https://archive.org/account/signup) | [Log in](https://archive.org/account/login)
[ Upload icon An illustration of a horizontal line over an up pointing arrow. Upload ](https://archive.org/create) Search icon An illustration of a magnifying glass.
Search icon An illustration of a magnifying glass.
###  Internet Archive Audio
[![](https://archive.org/services/img/etree)Live Music Archive](https://archive.org/details/etree) [![](https://archive.org/services/img/librivoxaudio)Librivox Free Audio](https://archive.org/details/librivoxaudio)
#### Featured
  * [All Audio](https://archive.org/details/audio)
  * [Grateful Dead](https://archive.org/details/GratefulDead)
  * [Netlabels](https://archive.org/details/netlabels)
  * [Old Time Radio](https://archive.org/details/oldtimeradio)
  * [78 RPMs and Cylinder Recordings](https://archive.org/details/78rpm)


#### Top
  * [Audio Books & Poetry](https://archive.org/details/audio_bookspoetry)
  * [Computers, Technology and Science](https://archive.org/details/audio_tech)
  * [Music, Arts & Culture](https://archive.org/details/audio_music)
  * [News & Public Affairs](https://archive.org/details/audio_news)
  * [Spirituality & Religion](https://archive.org/details/audio_religion)
  * [Podcasts](https://archive.org/details/podcasts)
  * [Radio News Archive](https://archive.org/details/radio)


###  Images
[![](https://archive.org/services/img/metropolitanmuseumofart-gallery)Metropolitan Museum](https://archive.org/details/metropolitanmuseumofart-gallery) [![](https://archive.org/services/img/clevelandart)Cleveland Museum of Art](https://archive.org/details/clevelandart)
#### Featured
  * [All Images](https://archive.org/details/image)
  * [Flickr Commons](https://archive.org/details/flickrcommons)
  * [Occupy Wall Street Flickr](https://archive.org/details/flickr-ows)
  * [Cover Art](https://archive.org/details/coverartarchive)
  * [USGS Maps](https://archive.org/details/maps_usgs)


#### Top
  * [NASA Images](https://archive.org/details/nasa)
  * [Solar System Collection](https://archive.org/details/solarsystemcollection)
  * [Ames Research Center](https://archive.org/details/amesresearchcenterimagelibrary)


###  Software
[![](https://archive.org/services/img/internetarcade)Internet Arcade](https://archive.org/details/internetarcade) [![](https://archive.org/services/img/consolelivingroom)Console Living Room](https://archive.org/details/consolelivingroom)
#### Featured
  * [All Software](https://archive.org/details/software)
  * [Old School Emulation](https://archive.org/details/tosec)
  * [MS-DOS Games](https://archive.org/details/softwarelibrary_msdos_games)
  * [Historical Software](https://archive.org/details/historicalsoftware)
  * [Classic PC Games](https://archive.org/details/classicpcgames)
  * [Software Library](https://archive.org/details/softwarelibrary)


#### Top
  * [Kodi Archive and Support File](https://archive.org/details/kodi_archive)
  * [Vintage Software](https://archive.org/details/vintagesoftware)
  * [APK](https://archive.org/details/apkarchive)
  * [MS-DOS](https://archive.org/details/softwarelibrary_msdos)
  * [CD-ROM Software](https://archive.org/details/cd-roms)
  * [CD-ROM Software Library](https://archive.org/details/cdromsoftware)
  * [Software Sites](https://archive.org/details/softwaresites)
  * [Tucows Software Library](https://archive.org/details/tucows)
  * [Shareware CD-ROMs](https://archive.org/details/cdbbsarchive)
  * [Software Capsules Compilation](https://archive.org/details/softwarecapsules)
  * [CD-ROM Images](https://archive.org/details/cdromimages)
  * [ZX Spectrum](https://archive.org/details/softwarelibrary_zx_spectrum)
  * [DOOM Level CD](https://archive.org/details/doom-cds)


###  Texts
[![](https://archive.org/images/widgetOL.png)Open Library](https://openlibrary.org/) [![](https://archive.org/services/img/americana)American Libraries](https://archive.org/details/americana)
#### Featured
  * [All Texts](https://archive.org/details/texts)
  * [Smithsonian Libraries](https://archive.org/details/smithsonian)
  * [FEDLINK (US)](https://archive.org/details/fedlink)
  * [Genealogy](https://archive.org/details/genealogy)
  * [Lincoln Collection](https://archive.org/details/lincolncollection)


#### Top
  * [American Libraries](https://archive.org/details/americana)
  * [Canadian Libraries](https://archive.org/details/toronto)
  * [Universal Library](https://archive.org/details/universallibrary)
  * [Project Gutenberg](https://archive.org/details/gutenberg)
  * [Children's Library](https://archive.org/details/iacl)
  * [Biodiversity Heritage Library](https://archive.org/details/biodiversity)
  * [Books by Language](https://archive.org/details/booksbylanguage)
  * [Additional Collections](https://archive.org/details/additional_collections)


###  Video
[![](https://archive.org/services/img/tv)TV News](https://archive.org/details/tv) [![](https://archive.org/services/img/911)Understanding 9/11](https://archive.org/details/911)
#### Featured
  * [All Video](https://archive.org/details/movies)
  * [Prelinger Archives](https://archive.org/details/prelinger)
  * [Democracy Now!](https://archive.org/details/democracy_now_vid)
  * [Occupy Wall Street](https://archive.org/details/occupywallstreet)
  * [TV NSA Clip Library](https://archive.org/details/nsa)


#### Top
  * [Animation & Cartoons](https://archive.org/details/animationandcartoons)
  * [Arts & Music](https://archive.org/details/artsandmusicvideos)
  * [Computers & Technology](https://archive.org/details/computersandtechvideos)
  * [Cultural & Academic Films](https://archive.org/details/culturalandacademicfilms)
  * [Ephemeral Films](https://archive.org/details/ephemera)
  * [Movies](https://archive.org/details/moviesandfilms)
  * [News & Public Affairs](https://archive.org/details/newsandpublicaffairs)
  * [Spirituality & Religion](https://archive.org/details/spiritualityandreligion)
  * [Sports Videos](https://archive.org/details/sports)
  * [Television](https://archive.org/details/television)
  * [Videogame Videos](https://archive.org/details/gamevideos)
  * [Vlogs](https://archive.org/details/vlogs)
  * [Youth Media](https://archive.org/details/youth_media)


Search the history of over __WB_PAGES_ARCHIVED__ [web pages](https://blog.archive.org/2016/10/23/defining-web-pages-web-sites-and-web-captures/) on the Internet. 
[ ](https://web.archive.org) Search the Wayback Machine
Search icon An illustration of a magnifying glass.
#### Mobile Apps
  * [Wayback Machine (iOS)](https://apps.apple.com/us/app/wayback-machine/id1201888313)
  * [Wayback Machine (Android)](https://play.google.com/store/apps/details?id=com.archive.waybackmachine&hl=en_US)


#### Browser Extensions
  * [Chrome](https://chrome.google.com/webstore/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak)
  * [Firefox](https://addons.mozilla.org/en-US/firefox/addon/wayback-machine_new/)
  * [Safari](https://apps.apple.com/us/app/wayback-machine/id1472432422?mt=12)
  * [Edge](https://microsoftedge.microsoft.com/addons/detail/wayback-machine/kjmickeoogghaimmomagaghnogelpcpn?hl=en-US)


#### Archive-It Subscription
  * [Explore the Collections](https://www.archive-it.org/explore)
  * [Learn More](https://www.archive-it.org/blog/learn-more/)
  * [Build Collections](https://www.archive-it.org/contact-us)


### Save Page Now
Capture a web page as it appears now for use as a trusted citation in the future.
Please enter a valid web address
  * [About](https://archive.org/about/)
  * [Blog](https://blog.archive.org)
  * [Projects](https://archive.org/projects/)
  * [Help](https://archive.org/about/faqs.php)
  * [Donate](https://archive.org/donate?origin=iawww-TopNavDonateButton)
  * [Contact](https://archive.org/about/contact)
  * [Jobs](https://archive.org/about/jobs)
  * [Volunteer](https://archive.org/about/volunteer-positions)
  * [People](https://archive.org/about/bios)


  * [ Sign up for free  ](https://archive.org/account/signup)
  * [ Log in  ](https://archive.org/account/login)


Search metadata  Search text contents  Search TV news captions  Search radio transcripts  Search archived web sites  [Advanced Search](https://archive.org/advancedsearch.php)
  * [About](https://archive.org/about/)
  * [Blog](https://blog.archive.org)
  * [Projects](https://archive.org/projects/)
  * [Help](https://archive.org/about/faqs.php)
  * [Donate Donate icon An illustration of a heart shape ](https://archive.org/donate?origin=iawww-TopNavDonateButton)
  * [Contact](https://archive.org/about/contact)
  * [Jobs](https://archive.org/about/jobs)
  * [Volunteer](https://archive.org/about/volunteer-positions)
  * [People](https://archive.org/about/bios)


[DONATE](http://archive.org/donate/?origin=wbwww-CalndrDonateButton)
[](https://web.archive.org/)
Latest Show All
## Hrm.
The Wayback Machine has not archived that URL.
Click here to search for all archived pages under [http://msdn.microsoft.com/en-us/library/](https://web.archive.org/web/*/http://msdn.microsoft.com/en-us/library/*). 
The Wayback Machine is an initiative of the [Internet Archive](https://archive.org/), a 501(c)(3) non-profit, building a digital library of Internet sites and other cultural artifacts in digital form.   
Other [projects](https://archive.org/projects/) include [Open Library](https://openlibrary.org/) & [archive-it.org](https://archive-it.org). 
Your use of the Wayback Machine is subject to the Internet Archive's [Terms of Use](https://archive.org/about/terms.php). 


---

## Wayback Machine

**Source:** http%3A//msdn.microsoft.com/en-us/library/bb313913.aspx
**Word Count:** 756

[Ask the publishers](https://change.org/LetReadersRead) to restore access to 500,000+ books.
Hamburger icon An icon used to represent a menu that can be toggled by interacting with this icon.
[ Internet Archive logo A line drawing of the Internet Archive headquarters building façade. ](https://archive.org/ "Go home")
[ Web icon An illustration of a computer application window Wayback Machine ](https://web.archive.org "Expand web menu") [ Texts icon An illustration of an open book.  Texts ](https://archive.org/details/texts "Expand texts menu") [ Video icon An illustration of two cells of a film strip. Video ](https://archive.org/details/movies "Expand video menu") [ Audio icon An illustration of an audio speaker.  Audio ](https://archive.org/details/audio "Expand audio menu") [ Software icon An illustration of a 3.5" floppy disk. Software ](https://archive.org/details/software "Expand software menu") [ Images icon An illustration of two photographs.  Images ](https://archive.org/details/image "Expand images menu") [ Donate icon An illustration of a heart shape  Donate ](https://archive.org/donate/ "Expand donate menu") [ Ellipses icon An illustration of text ellipses.  More ](https://archive.org/about/ "Expand more menu")
[ Donate icon An illustration of a heart shape "Donate to the archive" ](https://archive.org/donate/?origin=iawww-mbhrt)
User icon An illustration of a person's head and chest.  [Sign up](https://archive.org/account/signup) | [Log in](https://archive.org/account/login)
[ Upload icon An illustration of a horizontal line over an up pointing arrow. Upload ](https://archive.org/create) Search icon An illustration of a magnifying glass.
Search icon An illustration of a magnifying glass.
###  Internet Archive Audio
[![](https://archive.org/services/img/etree)Live Music Archive](https://archive.org/details/etree) [![](https://archive.org/services/img/librivoxaudio)Librivox Free Audio](https://archive.org/details/librivoxaudio)
#### Featured
  * [All Audio](https://archive.org/details/audio)
  * [Grateful Dead](https://archive.org/details/GratefulDead)
  * [Netlabels](https://archive.org/details/netlabels)
  * [Old Time Radio](https://archive.org/details/oldtimeradio)
  * [78 RPMs and Cylinder Recordings](https://archive.org/details/78rpm)


#### Top
  * [Audio Books & Poetry](https://archive.org/details/audio_bookspoetry)
  * [Computers, Technology and Science](https://archive.org/details/audio_tech)
  * [Music, Arts & Culture](https://archive.org/details/audio_music)
  * [News & Public Affairs](https://archive.org/details/audio_news)
  * [Spirituality & Religion](https://archive.org/details/audio_religion)
  * [Podcasts](https://archive.org/details/podcasts)
  * [Radio News Archive](https://archive.org/details/radio)


###  Images
[![](https://archive.org/services/img/metropolitanmuseumofart-gallery)Metropolitan Museum](https://archive.org/details/metropolitanmuseumofart-gallery) [![](https://archive.org/services/img/clevelandart)Cleveland Museum of Art](https://archive.org/details/clevelandart)
#### Featured
  * [All Images](https://archive.org/details/image)
  * [Flickr Commons](https://archive.org/details/flickrcommons)
  * [Occupy Wall Street Flickr](https://archive.org/details/flickr-ows)
  * [Cover Art](https://archive.org/details/coverartarchive)
  * [USGS Maps](https://archive.org/details/maps_usgs)


#### Top
  * [NASA Images](https://archive.org/details/nasa)
  * [Solar System Collection](https://archive.org/details/solarsystemcollection)
  * [Ames Research Center](https://archive.org/details/amesresearchcenterimagelibrary)


###  Software
[![](https://archive.org/services/img/internetarcade)Internet Arcade](https://archive.org/details/internetarcade) [![](https://archive.org/services/img/consolelivingroom)Console Living Room](https://archive.org/details/consolelivingroom)
#### Featured
  * [All Software](https://archive.org/details/software)
  * [Old School Emulation](https://archive.org/details/tosec)
  * [MS-DOS Games](https://archive.org/details/softwarelibrary_msdos_games)
  * [Historical Software](https://archive.org/details/historicalsoftware)
  * [Classic PC Games](https://archive.org/details/classicpcgames)
  * [Software Library](https://archive.org/details/softwarelibrary)


#### Top
  * [Kodi Archive and Support File](https://archive.org/details/kodi_archive)
  * [Vintage Software](https://archive.org/details/vintagesoftware)
  * [APK](https://archive.org/details/apkarchive)
  * [MS-DOS](https://archive.org/details/softwarelibrary_msdos)
  * [CD-ROM Software](https://archive.org/details/cd-roms)
  * [CD-ROM Software Library](https://archive.org/details/cdromsoftware)
  * [Software Sites](https://archive.org/details/softwaresites)
  * [Tucows Software Library](https://archive.org/details/tucows)
  * [Shareware CD-ROMs](https://archive.org/details/cdbbsarchive)
  * [Software Capsules Compilation](https://archive.org/details/softwarecapsules)
  * [CD-ROM Images](https://archive.org/details/cdromimages)
  * [ZX Spectrum](https://archive.org/details/softwarelibrary_zx_spectrum)
  * [DOOM Level CD](https://archive.org/details/doom-cds)


###  Texts
[![](https://archive.org/images/widgetOL.png)Open Library](https://openlibrary.org/) [![](https://archive.org/services/img/americana)American Libraries](https://archive.org/details/americana)
#### Featured
  * [All Texts](https://archive.org/details/texts)
  * [Smithsonian Libraries](https://archive.org/details/smithsonian)
  * [FEDLINK (US)](https://archive.org/details/fedlink)
  * [Genealogy](https://archive.org/details/genealogy)
  * [Lincoln Collection](https://archive.org/details/lincolncollection)


#### Top
  * [American Libraries](https://archive.org/details/americana)
  * [Canadian Libraries](https://archive.org/details/toronto)
  * [Universal Library](https://archive.org/details/universallibrary)
  * [Project Gutenberg](https://archive.org/details/gutenberg)
  * [Children's Library](https://archive.org/details/iacl)
  * [Biodiversity Heritage Library](https://archive.org/details/biodiversity)
  * [Books by Language](https://archive.org/details/booksbylanguage)
  * [Additional Collections](https://archive.org/details/additional_collections)


###  Video
[![](https://archive.org/services/img/tv)TV News](https://archive.org/details/tv) [![](https://archive.org/services/img/911)Understanding 9/11](https://archive.org/details/911)
#### Featured
  * [All Video](https://archive.org/details/movies)
  * [Prelinger Archives](https://archive.org/details/prelinger)
  * [Democracy Now!](https://archive.org/details/democracy_now_vid)
  * [Occupy Wall Street](https://archive.org/details/occupywallstreet)
  * [TV NSA Clip Library](https://archive.org/details/nsa)


#### Top
  * [Animation & Cartoons](https://archive.org/details/animationandcartoons)
  * [Arts & Music](https://archive.org/details/artsandmusicvideos)
  * [Computers & Technology](https://archive.org/details/computersandtechvideos)
  * [Cultural & Academic Films](https://archive.org/details/culturalandacademicfilms)
  * [Ephemeral Films](https://archive.org/details/ephemera)
  * [Movies](https://archive.org/details/moviesandfilms)
  * [News & Public Affairs](https://archive.org/details/newsandpublicaffairs)
  * [Spirituality & Religion](https://archive.org/details/spiritualityandreligion)
  * [Sports Videos](https://archive.org/details/sports)
  * [Television](https://archive.org/details/television)
  * [Videogame Videos](https://archive.org/details/gamevideos)
  * [Vlogs](https://archive.org/details/vlogs)
  * [Youth Media](https://archive.org/details/youth_media)


Search the history of over __WB_PAGES_ARCHIVED__ [web pages](https://blog.archive.org/2016/10/23/defining-web-pages-web-sites-and-web-captures/) on the Internet. 
[ ](https://web.archive.org) Search the Wayback Machine
Search icon An illustration of a magnifying glass.
#### Mobile Apps
  * [Wayback Machine (iOS)](https://apps.apple.com/us/app/wayback-machine/id1201888313)
  * [Wayback Machine (Android)](https://play.google.com/store/apps/details?id=com.archive.waybackmachine&hl=en_US)


#### Browser Extensions
  * [Chrome](https://chrome.google.com/webstore/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak)
  * [Firefox](https://addons.mozilla.org/en-US/firefox/addon/wayback-machine_new/)
  * [Safari](https://apps.apple.com/us/app/wayback-machine/id1472432422?mt=12)
  * [Edge](https://microsoftedge.microsoft.com/addons/detail/wayback-machine/kjmickeoogghaimmomagaghnogelpcpn?hl=en-US)


#### Archive-It Subscription
  * [Explore the Collections](https://www.archive-it.org/explore)
  * [Learn More](https://www.archive-it.org/blog/learn-more/)
  * [Build Collections](https://www.archive-it.org/contact-us)


### Save Page Now
Capture a web page as it appears now for use as a trusted citation in the future.
Please enter a valid web address
  * [About](https://archive.org/about/)
  * [Blog](https://blog.archive.org)
  * [Projects](https://archive.org/projects/)
  * [Help](https://archive.org/about/faqs.php)
  * [Donate](https://archive.org/donate?origin=iawww-TopNavDonateButton)
  * [Contact](https://archive.org/about/contact)
  * [Jobs](https://archive.org/about/jobs)
  * [Volunteer](https://archive.org/about/volunteer-positions)
  * [People](https://archive.org/about/bios)


  * [ Sign up for free  ](https://archive.org/account/signup)
  * [ Log in  ](https://archive.org/account/login)


Search metadata  Search text contents  Search TV news captions  Search radio transcripts  Search archived web sites  [Advanced Search](https://archive.org/advancedsearch.php)
  * [About](https://archive.org/about/)
  * [Blog](https://blog.archive.org)
  * [Projects](https://archive.org/projects/)
  * [Help](https://archive.org/about/faqs.php)
  * [Donate Donate icon An illustration of a heart shape ](https://archive.org/donate?origin=iawww-TopNavDonateButton)
  * [Contact](https://archive.org/about/contact)
  * [Jobs](https://archive.org/about/jobs)
  * [Volunteer](https://archive.org/about/volunteer-positions)
  * [People](https://archive.org/about/bios)


[DONATE](http://archive.org/donate/?origin=wbwww-CalndrDonateButton)
[](https://web.archive.org/)
Latest Show All
## Hrm.
The Wayback Machine has not archived that URL.
Click here to search for all archived pages under [http://msdn.microsoft.com/en-us/library/](https://web.archive.org/web/*/http://msdn.microsoft.com/en-us/library/*). 
The Wayback Machine is an initiative of the [Internet Archive](https://archive.org/), a 501(c)(3) non-profit, building a digital library of Internet sites and other cultural artifacts in digital form.   
Other [projects](https://archive.org/projects/) include [Open Library](https://openlibrary.org/) & [archive-it.org](https://archive-it.org). 
Your use of the Wayback Machine is subject to the Internet Archive's [Terms of Use](https://archive.org/about/terms.php). 


---

## vfetch (xvs_3_0, xps_3_0)

**Source:** https://web.archive.org/web/20100423061946/http%3A//msdn.microsoft.com/en-us/library/bb313960.aspx
**Word Count:** 186

XNA Game Studio 3.1
vfetch (xvs_3_0, xps_3_0)
Fetches data from a vertex buffer using a semantic.  ```
vfetch dest, src1, Semantic [, name = value, ...]
```
  
---  
# Name-Value Pair 

**RoundIndex** = **bool** 
    If **RoundIndex** is **true** , the _src1_ index value is rounded to the nearest integer; otherwise, the _src1_ index value is floored. The default value is **false**. 

**ExpAdjust** = **int** 
    Data multiplier. This value must be an integer between −32 and 31. The fetched vertex data is multiplied by two raised to the **ExpAdjust** value. The default value is 0 (the data is multiplied by one—no change). 

**UseTextureCache** = **bool** 
    If **UseTextureCache** is **true** , the **vfetch (xvs_3_0, xps_3_0)** instruction caches its data in the texture cache; otherwise, the instruction caches its data in the vertex cachce. The default value is **false**.
* * *
  
[MSDN Library](https://web.archive.org/web/20100302145413/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20100302145413/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20100302145413/http://msdn.microsoft.com/en-us/library/aa139594.aspx)  
[XNA Game Studio 3.1](https://web.archive.org/web/20100302145413/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20100302145413/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20100302145413/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20100302145413/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100302145413/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100302145413/http://msdn.microsoft.com/en-us/library/bb313961.aspx)  
[Fetch Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100302145413/http://msdn.microsoft.com/en-us/library/bb313942.aspx)  
[vfetch (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100302145413/http://msdn.microsoft.com/en-us/library/bb313960.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20100302145413im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

## ALU Vector Instructions (xvs_3_0, xps_3_0)

**Source:** http://msdn.microsoft.com/en-us/library/bb313916.aspx
**Word Count:** 607

[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")
[2 captures](https://web.archive.org/web/20100425014442*/http://msdn.microsoft.com/en-us/library/bb313916.aspx "See a list of every capture for this URL")
25 Apr 2010 - 03 Jul 2010
[ ](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313916.aspx)
Mar | APR | [**Jul**](https://web.archive.org/web/20100703154652/http://msdn.microsoft.com:80/en-us/library/bb313916.aspx "03 Jul 2010")  
---|---|---  
![Previous capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_prv_off.png) | 25 | [![Next capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_nxt_on.png)](https://web.archive.org/web/20100703154652/http://msdn.microsoft.com:80/en-us/library/bb313916.aspx "15:46:52 Jul 03, 2010")  
2009 | 2010 | 2011  
success
fail
[ ](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313916.aspx "Share via My Web Archive") [ ](https://archive.org/account/login.php "Sign In") [](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine") [](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313916.aspx#close "Close the toolbar")
[ ](https://web.archive.org/web/20100425014442/http://web.archive.org/screenshot/http://msdn.microsoft.com/en-us/library/bb313916.aspx "screenshot") [ ](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313916.aspx "video") [](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313916.aspx "Share on Facebook") [](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313916.aspx "Share on Twitter")
[About this capture](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313916.aspx#expand)
COLLECTED BY
[Alexa Crawls](https://archive.org/details/alexacrawls)
[Alexa Internet](http://www.alexa.com/) has been donating their crawl data to the Internet Archive. Flowing in every day, these data are added to the [Wayback Machine](http://web.archive.org/) after an embargo period. 
Collection: [alexa_web_2010](https://archive.org/details/alexa_web_2010)
TIMESTAMPS
![loading](https://web-static.archive.org/_static/images/loading.gif)
The Wayback Machine - https://web.archive.org/web/20100425014442/http://msdn.microsoft.com:80/en-us/library/bb313916.aspx
XNA Game Studio 3.1
ALU Vector Instructions (xvs_3_0, xps_3_0)
Instruction | Description  
---|---  
[add](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313917.aspx) |  Per-component add.  
[cndeq](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313918.aspx) |  Per-component conditional move when the component is zero.  
[cndge](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313919.aspx) |  Per-component conditional move when the component is greater than or equal to zero.  
[cndgt](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313920.aspx) |  Per-component conditional move when the component is greater than zero.  
[cube](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313921.aspx) |  Helps to setup the input needed to allow the [tfetchCube](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313959.aspx) instruction to perform a cube map texture lookup.  
[dp2add](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313922.aspx) |  Two-component dot product with addition. The result is replicated into all channels.  
[dp3](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313923.aspx) |  Three-component dot product. The result is replicated into all channels.  
[dp4](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313924.aspx) |  Four-component dot product. The result is replicated into all channels.  
[dst](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313925.aspx) |  Computes the distance vector.  
[floor](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313926.aspx) |  Computes the greatest integer that is less than or equal to the component.  
[frc](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313927.aspx) |  Computes the fractional part of each component.  
[mad](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313928.aspx) |  Per-component multiply then add.  
[max](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313929.aspx) |  Per-component maximum.  
[max4](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313930.aspx) |  Computes the maximum of the components of the source. The result is replicated into all channels.  
[maxa](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313931.aspx) |  Updates the address register (a0) with the w-component of the source register, rounded to the nearest integer. It then computes the per-component maximum.  
[min](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313932.aspx) |  Per-component minimum.  
[mov](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313933.aspx) |  Moves data between registers.  
[mova](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313934.aspx) |  Moves data between registers and updates the address register (a0) with the w-component of the source register, rounded to the nearest integer.  
[mul](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313935.aspx) |  Per-component multiply.  
[nop](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313936.aspx) |  No operation is performed on the vector ALU.  
[seq](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313937.aspx) |  Sets the destination components equal to one if the corresponding source components are equal.  
[sge](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313938.aspx) |  Sets the destination components equal to one if the corresponding component of the first source is greater than or equal to the corresponding component of the second source.  
[sgt](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313939.aspx) |  Sets the destination components equal to one if the corresponding component of the first source is greater than the corresponding component of the second source.  
[sne](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313940.aspx) |  Sets the destination components equal to one if the corresponding source components are unequal.  
[trunc](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313941.aspx) |  Truncates each component of the source register.  
See Also
* * *
#### Concepts
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  

  
[add (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313917.aspx)  
[cndeq (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313918.aspx)  
[cndge (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313919.aspx)  
[cndgt (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313920.aspx)  
[cube (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313921.aspx)  
[dp2add (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313922.aspx)  
[dp3 (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313923.aspx)  
[dp4 (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313924.aspx)  
[dst (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313925.aspx)  
[floor (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313926.aspx)  
[frc (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313927.aspx)  
[mad (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313928.aspx)  
[max (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313929.aspx)  
[maxa (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313931.aspx)  
[max4 (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313930.aspx)  
[min (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313932.aspx)  
[mov (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313933.aspx)  
[mova (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313934.aspx)  
[mul (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313935.aspx)  
[nop (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313936.aspx)  
[seq (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313937.aspx)  
[sge (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313938.aspx)  
[sgt (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313939.aspx)  
[sne (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313940.aspx)  
[trunc (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313941.aspx)
* * *
  
[MSDN Library](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/aa468128.aspx)  
[XNA Game Studio 3.1](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313961.aspx)  
[ALU Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313878.aspx)  
[ALU Vector Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313916.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20100425014442im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

## ALU Instructions (xvs_3_0, xps_3_0)

**Source:** http://msdn.microsoft.com/en-us/library/bb313878.aspx
**Word Count:** 214

[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")
[1 capture](https://web.archive.org/web/20100423054747*/http://msdn.microsoft.com/en-us/library/bb313878.aspx "See a list of every capture for this URL")
23 Apr 2010
[ ](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313878.aspx)
Mar | APR | May  
---|---|---  
![Previous capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_prv_off.png) | 23 | ![Next capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_nxt_off.png)  
2009 | 2010 | 2011  
success
fail
[ ](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313878.aspx "Share via My Web Archive") [ ](https://archive.org/account/login.php "Sign In") [](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine") [](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313878.aspx#close "Close the toolbar")
[ ](https://web.archive.org/web/20100423054747/http://web.archive.org/screenshot/http://msdn.microsoft.com/en-us/library/bb313878.aspx "screenshot") [ ](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313878.aspx "video") [](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313878.aspx "Share on Facebook") [](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313878.aspx "Share on Twitter")
[About this capture](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313878.aspx#expand)
COLLECTED BY
[Alexa Crawls](https://archive.org/details/alexacrawls)
[Alexa Internet](http://www.alexa.com/) has been donating their crawl data to the Internet Archive. Flowing in every day, these data are added to the [Wayback Machine](http://web.archive.org/) after an embargo period. 
Collection: [alexa_web_2010](https://archive.org/details/alexa_web_2010)
TIMESTAMPS
![loading](https://web-static.archive.org/_static/images/loading.gif)
The Wayback Machine - https://web.archive.org/web/20100423054747/http://msdn.microsoft.com:80/en-us/library/bb313878.aspx
XNA Game Studio 3.1
ALU Instructions (xvs_3_0, xps_3_0)
The ALU has both a vector unit and a scalar unit. 
# In This Section 

[Vector Instructions](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313916.aspx) 
    Documentation for the ALU vector instructions. 

[Scalar Instructions](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313879.aspx) 
    Documentation for the ALU scalar instructions.
  
[ALU Vector Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313916.aspx)  
[ALU Scalar Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313879.aspx)
* * *
  
[MSDN Library](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/aa468128.aspx)  
[XNA Game Studio 3.1](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313961.aspx)  
[ALU Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100423054747/http://msdn.microsoft.com/en-us/library/bb313878.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20100423054747im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

## Wayback Machine

**Source:** http://msdn.microsoft.com/en-us/library/bb313891.aspx
**Word Count:** 756

[Ask the publishers](https://change.org/LetReadersRead) to restore access to 500,000+ books.
Hamburger icon An icon used to represent a menu that can be toggled by interacting with this icon.
[ Internet Archive logo A line drawing of the Internet Archive headquarters building façade. ](https://archive.org/ "Go home")
[ Web icon An illustration of a computer application window Wayback Machine ](https://web.archive.org "Expand web menu") [ Texts icon An illustration of an open book.  Texts ](https://archive.org/details/texts "Expand texts menu") [ Video icon An illustration of two cells of a film strip. Video ](https://archive.org/details/movies "Expand video menu") [ Audio icon An illustration of an audio speaker.  Audio ](https://archive.org/details/audio "Expand audio menu") [ Software icon An illustration of a 3.5" floppy disk. Software ](https://archive.org/details/software "Expand software menu") [ Images icon An illustration of two photographs.  Images ](https://archive.org/details/image "Expand images menu") [ Donate icon An illustration of a heart shape  Donate ](https://archive.org/donate/ "Expand donate menu") [ Ellipses icon An illustration of text ellipses.  More ](https://archive.org/about/ "Expand more menu")
[ Donate icon An illustration of a heart shape "Donate to the archive" ](https://archive.org/donate/?origin=iawww-mbhrt)
User icon An illustration of a person's head and chest.  [Sign up](https://archive.org/account/signup) | [Log in](https://archive.org/account/login)
[ Upload icon An illustration of a horizontal line over an up pointing arrow. Upload ](https://archive.org/create) Search icon An illustration of a magnifying glass.
Search icon An illustration of a magnifying glass.
###  Internet Archive Audio
[![](https://archive.org/services/img/etree)Live Music Archive](https://archive.org/details/etree) [![](https://archive.org/services/img/librivoxaudio)Librivox Free Audio](https://archive.org/details/librivoxaudio)
#### Featured
  * [All Audio](https://archive.org/details/audio)
  * [Grateful Dead](https://archive.org/details/GratefulDead)
  * [Netlabels](https://archive.org/details/netlabels)
  * [Old Time Radio](https://archive.org/details/oldtimeradio)
  * [78 RPMs and Cylinder Recordings](https://archive.org/details/78rpm)


#### Top
  * [Audio Books & Poetry](https://archive.org/details/audio_bookspoetry)
  * [Computers, Technology and Science](https://archive.org/details/audio_tech)
  * [Music, Arts & Culture](https://archive.org/details/audio_music)
  * [News & Public Affairs](https://archive.org/details/audio_news)
  * [Spirituality & Religion](https://archive.org/details/audio_religion)
  * [Podcasts](https://archive.org/details/podcasts)
  * [Radio News Archive](https://archive.org/details/radio)


###  Images
[![](https://archive.org/services/img/metropolitanmuseumofart-gallery)Metropolitan Museum](https://archive.org/details/metropolitanmuseumofart-gallery) [![](https://archive.org/services/img/clevelandart)Cleveland Museum of Art](https://archive.org/details/clevelandart)
#### Featured
  * [All Images](https://archive.org/details/image)
  * [Flickr Commons](https://archive.org/details/flickrcommons)
  * [Occupy Wall Street Flickr](https://archive.org/details/flickr-ows)
  * [Cover Art](https://archive.org/details/coverartarchive)
  * [USGS Maps](https://archive.org/details/maps_usgs)


#### Top
  * [NASA Images](https://archive.org/details/nasa)
  * [Solar System Collection](https://archive.org/details/solarsystemcollection)
  * [Ames Research Center](https://archive.org/details/amesresearchcenterimagelibrary)


###  Software
[![](https://archive.org/services/img/internetarcade)Internet Arcade](https://archive.org/details/internetarcade) [![](https://archive.org/services/img/consolelivingroom)Console Living Room](https://archive.org/details/consolelivingroom)
#### Featured
  * [All Software](https://archive.org/details/software)
  * [Old School Emulation](https://archive.org/details/tosec)
  * [MS-DOS Games](https://archive.org/details/softwarelibrary_msdos_games)
  * [Historical Software](https://archive.org/details/historicalsoftware)
  * [Classic PC Games](https://archive.org/details/classicpcgames)
  * [Software Library](https://archive.org/details/softwarelibrary)


#### Top
  * [Kodi Archive and Support File](https://archive.org/details/kodi_archive)
  * [Vintage Software](https://archive.org/details/vintagesoftware)
  * [APK](https://archive.org/details/apkarchive)
  * [MS-DOS](https://archive.org/details/softwarelibrary_msdos)
  * [CD-ROM Software](https://archive.org/details/cd-roms)
  * [CD-ROM Software Library](https://archive.org/details/cdromsoftware)
  * [Software Sites](https://archive.org/details/softwaresites)
  * [Tucows Software Library](https://archive.org/details/tucows)
  * [Shareware CD-ROMs](https://archive.org/details/cdbbsarchive)
  * [Software Capsules Compilation](https://archive.org/details/softwarecapsules)
  * [CD-ROM Images](https://archive.org/details/cdromimages)
  * [ZX Spectrum](https://archive.org/details/softwarelibrary_zx_spectrum)
  * [DOOM Level CD](https://archive.org/details/doom-cds)


###  Texts
[![](https://archive.org/images/widgetOL.png)Open Library](https://openlibrary.org/) [![](https://archive.org/services/img/americana)American Libraries](https://archive.org/details/americana)
#### Featured
  * [All Texts](https://archive.org/details/texts)
  * [Smithsonian Libraries](https://archive.org/details/smithsonian)
  * [FEDLINK (US)](https://archive.org/details/fedlink)
  * [Genealogy](https://archive.org/details/genealogy)
  * [Lincoln Collection](https://archive.org/details/lincolncollection)


#### Top
  * [American Libraries](https://archive.org/details/americana)
  * [Canadian Libraries](https://archive.org/details/toronto)
  * [Universal Library](https://archive.org/details/universallibrary)
  * [Project Gutenberg](https://archive.org/details/gutenberg)
  * [Children's Library](https://archive.org/details/iacl)
  * [Biodiversity Heritage Library](https://archive.org/details/biodiversity)
  * [Books by Language](https://archive.org/details/booksbylanguage)
  * [Additional Collections](https://archive.org/details/additional_collections)


###  Video
[![](https://archive.org/services/img/tv)TV News](https://archive.org/details/tv) [![](https://archive.org/services/img/911)Understanding 9/11](https://archive.org/details/911)
#### Featured
  * [All Video](https://archive.org/details/movies)
  * [Prelinger Archives](https://archive.org/details/prelinger)
  * [Democracy Now!](https://archive.org/details/democracy_now_vid)
  * [Occupy Wall Street](https://archive.org/details/occupywallstreet)
  * [TV NSA Clip Library](https://archive.org/details/nsa)


#### Top
  * [Animation & Cartoons](https://archive.org/details/animationandcartoons)
  * [Arts & Music](https://archive.org/details/artsandmusicvideos)
  * [Computers & Technology](https://archive.org/details/computersandtechvideos)
  * [Cultural & Academic Films](https://archive.org/details/culturalandacademicfilms)
  * [Ephemeral Films](https://archive.org/details/ephemera)
  * [Movies](https://archive.org/details/moviesandfilms)
  * [News & Public Affairs](https://archive.org/details/newsandpublicaffairs)
  * [Spirituality & Religion](https://archive.org/details/spiritualityandreligion)
  * [Sports Videos](https://archive.org/details/sports)
  * [Television](https://archive.org/details/television)
  * [Videogame Videos](https://archive.org/details/gamevideos)
  * [Vlogs](https://archive.org/details/vlogs)
  * [Youth Media](https://archive.org/details/youth_media)


Search the history of over __WB_PAGES_ARCHIVED__ [web pages](https://blog.archive.org/2016/10/23/defining-web-pages-web-sites-and-web-captures/) on the Internet. 
[ ](https://web.archive.org) Search the Wayback Machine
Search icon An illustration of a magnifying glass.
#### Mobile Apps
  * [Wayback Machine (iOS)](https://apps.apple.com/us/app/wayback-machine/id1201888313)
  * [Wayback Machine (Android)](https://play.google.com/store/apps/details?id=com.archive.waybackmachine&hl=en_US)


#### Browser Extensions
  * [Chrome](https://chrome.google.com/webstore/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak)
  * [Firefox](https://addons.mozilla.org/en-US/firefox/addon/wayback-machine_new/)
  * [Safari](https://apps.apple.com/us/app/wayback-machine/id1472432422?mt=12)
  * [Edge](https://microsoftedge.microsoft.com/addons/detail/wayback-machine/kjmickeoogghaimmomagaghnogelpcpn?hl=en-US)


#### Archive-It Subscription
  * [Explore the Collections](https://www.archive-it.org/explore)
  * [Learn More](https://www.archive-it.org/blog/learn-more/)
  * [Build Collections](https://www.archive-it.org/contact-us)


### Save Page Now
Capture a web page as it appears now for use as a trusted citation in the future.
Please enter a valid web address
  * [About](https://archive.org/about/)
  * [Blog](https://blog.archive.org)
  * [Projects](https://archive.org/projects/)
  * [Help](https://archive.org/about/faqs.php)
  * [Donate](https://archive.org/donate?origin=iawww-TopNavDonateButton)
  * [Contact](https://archive.org/about/contact)
  * [Jobs](https://archive.org/about/jobs)
  * [Volunteer](https://archive.org/about/volunteer-positions)
  * [People](https://archive.org/about/bios)


  * [ Sign up for free  ](https://archive.org/account/signup)
  * [ Log in  ](https://archive.org/account/login)


Search metadata  Search text contents  Search TV news captions  Search radio transcripts  Search archived web sites  [Advanced Search](https://archive.org/advancedsearch.php)
  * [About](https://archive.org/about/)
  * [Blog](https://blog.archive.org)
  * [Projects](https://archive.org/projects/)
  * [Help](https://archive.org/about/faqs.php)
  * [Donate Donate icon An illustration of a heart shape ](https://archive.org/donate?origin=iawww-TopNavDonateButton)
  * [Contact](https://archive.org/about/contact)
  * [Jobs](https://archive.org/about/jobs)
  * [Volunteer](https://archive.org/about/volunteer-positions)
  * [People](https://archive.org/about/bios)


[DONATE](http://archive.org/donate/?origin=wbwww-CalndrDonateButton)
[](https://web.archive.org/)
Latest Show All
## Hrm.
The Wayback Machine has not archived that URL.
Click here to search for all archived pages under [http://msdn.microsoft.com/en-us/library/](https://web.archive.org/web/*/http://msdn.microsoft.com/en-us/library/*). 
The Wayback Machine is an initiative of the [Internet Archive](https://archive.org/), a 501(c)(3) non-profit, building a digital library of Internet sites and other cultural artifacts in digital form.   
Other [projects](https://archive.org/projects/) include [Open Library](https://openlibrary.org/) & [archive-it.org](https://archive-it.org). 
Your use of the Wayback Machine is subject to the Internet Archive's [Terms of Use](https://archive.org/about/terms.php). 


---

## tfetch1D (xvs_3_0, xps_3_0)

**Source:** http://msdn.microsoft.com/en-us/library/bb313956.aspx
**Word Count:** 1105

[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")
[1 capture](https://web.archive.org/web/20090511231340*/http://msdn.microsoft.com/en-us/library/bb313956.aspx "See a list of every capture for this URL")
11 May 2009
[ ](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313956.aspx)
Apr | MAY | Jun  
---|---|---  
![Previous capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_prv_off.png) | 11 | ![Next capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_nxt_off.png)  
2008 | 2009 | 2010  
success
fail
[ ](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313956.aspx "Share via My Web Archive") [ ](https://archive.org/account/login.php "Sign In") [](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine") [](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313956.aspx#close "Close the toolbar")
[ ](https://web.archive.org/web/20090511231340/http://web.archive.org/screenshot/http://msdn.microsoft.com/en-us/library/bb313956.aspx "screenshot") [ ](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313956.aspx "video") [](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313956.aspx "Share on Facebook") [](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313956.aspx "Share on Twitter")
[About this capture](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313956.aspx#expand)
COLLECTED BY
[Alexa Crawls](https://archive.org/details/alexacrawls)
[Alexa Internet](http://www.alexa.com/) has been donating their crawl data to the Internet Archive. Flowing in every day, these data are added to the [Wayback Machine](http://web.archive.org/) after an embargo period. 
Collection: [alexa_web_2009](https://archive.org/details/alexa_web_2009)
TIMESTAMPS
![loading](https://web-static.archive.org/_static/images/loading.gif)
The Wayback Machine - https://web.archive.org/web/20090511231340/http://msdn.microsoft.com:80/en-us/library/bb313956.aspx
XNA Game Studio 3.0
tfetch1D (xvs_3_0, xps_3_0)
Fetches sample data from a 1D texture.  ```
tfetch1D dest, src1, fetchConst [, name = value, ...]
```
  
---  
# Name-Value Pair 

**UnnormalizedTextureCoords** = **bool** 
    If **UnnormalizedTextureCoords** is **true** , texture coordinates should range between 0 and the dimensions of the texture; otherwise, the texture coordinates should range beween 0.0f and 1.0f. The default value is **false**. 

**MagFilter** = **enum** 
    
Filter used when the texture is magnified. **MagFilter** must be one of the following values.
Value | Description  
---|---  
point | Point filter. The texel with coordinates nearest to the desired pixel value is used.  
linear | Bilinear interpolation filter. A weighted average of a 22 area of texels surrounding the desired pixel is used.  
keep | Use the filtering set up by Direct3D. This is the default value. 

**MinFilter** = **enum** 
      
Filter used when the texture is minified. **MinFilter** must be one of the following values.
Value | Description  
---|---  
point | Point filter. The texel with coordinates nearest to the desired pixel value is used.  
linear | Bilinear interpolation filter. A weighted average of a 22 area of texels surrounding the desired pixel is used.  
keep | Use the filtering set up by Direct3D. This is the default value. 

**MipFilter** = **enum** 
      
Filter used between mipmap levels. **MipFilter** must be one of the following values.
Value | Description  
---|---  
point | Point filter. The mipmap with coordinates nearest to the desired pixel value is used.  
linear | Trilinear interpolation filtering is used as a mipmap filter, using the texels of the two nearest mipmap textures.  
keep | Use the filtering set up by Direct3D. This is the default value. 

**AnisoFilter** = **enum** 
      
Anisotropic filter used for minification and magnification. **AnisoFilter** must be one of the following values.
Value | Description  
---|---  
disabled | No anisotropic filtering.  
max1to1 | Use at most 1 sample for anisotropic filtering.  
max2to1 | Use at most 2 samples for anisotropic filtering.  
max4to1 | Use at most 4 samples for anisotropic filtering.  
max8to1 | Use at most 8 samples for anisotropic filtering.  
max16to1 | Use at most 16 samples for anisotropic filtering.  
keep | Use the anisotropic filtering as set up by Direct3D. This is the default value. 

**UseComputedLOD** = **bool** 
    If **UseComputedLOD** is **true** , the shader will use the LOD computed in the texture pipeline. The default value is **true**. For more details, see [Computing the LOD](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313956.aspx). 

**UseRegisterLOD** = **bool** 
    If **UseRegisterLOD** is **true** , the shader will use the LOD set by [setTexLOD](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313955.aspx). The default value is **false**. For more details, see [Computing the LOD](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313956.aspx). 

**LODBias** = **float** 
    Bias to add to the LOD. The _value_ must be a number between −4.0 and 3.9375. In addition, _value_ must be an integer multiple of 0.0625. The default value is 0.0f. For more details, see [Computing the LOD](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313956.aspx). 

**OffsetX** = **float** 
    Value added to the x-component of the texel address right before sampling. The _value_ must be between −8.0f and 7.5f. In addition, _value_ must be an integer multiple of 0.5f. The default value is 0.0f. 

**OffsetY** = **float** 
    Value added to the y-component of the texel address right before sampling. The _value_ must be between −8.0f and 7.5f. In addition, _value_ must be an integer multiple of 0.5f. The default value is 0.0f. 

**OffsetZ** = **float** 
    Value added to the z-component of the texel address right before sampling. The _value_ must be between −8.0f and 7.5f. In addition, _value_ must be an integer multiple of 0.5f. The default value is 0.0f. 

**FetchValidOnly** = **bool** 
      
Performance booster that determines if pixel data should be fetched for pixels outside of the current primitive. The default value is **true**. For vertex shaders, **FetchValidOnly** should always be **true**. For pixel shaders, **FetchValidOnly** should be **true** , unless the result of the **tfetch** instruction is used to calculate a gradient, by using [getGradients](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb464129.aspx) or a **tfetch** instruction with **UseComputedLOD** set to **true**. 
Gradient information is calculated by running a 2×2 quad of pixel shaders and computing the difference between the resulting pixels. At the edges of triangles, there are situations where one or more of the pixel shaders in the quad lies outside the boundary of the triangle, and so its computed values won't be output. The **FetchValidOnly** value is used to tell the hardware that it doesn't have to fetch the pixel data for these out-of-bounds pixel shaders. When **FetchValidOnly** is **true** , data will be fetched only for those pixels that are valid (inside the triangle), which speeds up the calculations.
In cases where the result of the texture fetch is itself used to calculate gradient information, all four pixel shaders in the quad are necessary to compute the gradients, and **FetchValidOnly** should be set to **false**.
![](https://web.archive.org/web/20090511231340im_/http://i.msdn.microsoft.com/Global/Images/clear.gif) Remarks 
The _src1_ register specifies the coordinates from which to fetch the sample data.
If **UnnormalizedTextureCoords** is **true** , you must set the [AddressU](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/microsoft.xna.framework.graphics.samplerstate.addressu.aspx) texture sampler state to a clamping mode such as [TextureAddressMode.Clamp](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/microsoft.xna.framework.graphics.textureaddressmode.aspx), rather than a wrapping mode. Using a wrapping mode will force normalized texture coordinates even if **UnnormalizedTextureCoords** is **true**.
To access access 1D textures that are wider than 8192 texels, you must use unnormalized texture coordinates.
![Bb313956.note\(en-US,XNAGameStudio.30\).gif](https://web.archive.org/web/20090511231340im_/http://i.msdn.microsoft.com/Bb313956.note\(en-US,XNAGameStudio.30\).gif)Note   
---  
To use the **tfetch1D (xvs_3_0, xps_3_0)** instruction in a vertex shader, **UseComputedLOD** must be **false** unless you manually set the gradients and set **UseRegisterGradients** to **true**.  
## Computing the LOD
The total LOD for a sample is additive and is based on what is enabled. The total LOD is determined by the LOD computed in the texture pipeline (if **UseComputedLOD** is **true**), the LOD set by [setTexLOD](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313955.aspx) (if **UseRegisterLOD** is **true**), and the **LODBias** value.
* * *
  
[MSDN Library](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/aa187935.aspx)  
[XNA Game Studio 3.0](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313961.aspx)  
[Fetch Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313942.aspx)  
[tfetch1D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090511231340/http://msdn.microsoft.com/en-us/library/bb313956.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20090511231340im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

## tfetch3D (xvs_3_0, xps_3_0)

**Source:** http://msdn.microsoft.com/en-us/library/bb313958.aspx
**Word Count:** 1163

[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")
[3 captures](https://web.archive.org/web/20100425013737*/http://msdn.microsoft.com/en-us/library/bb313958.aspx "See a list of every capture for this URL")
12 May 2009 - 05 Jul 2010
[ ](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313958.aspx)
[**May**](https://web.archive.org/web/20090512001222/http://msdn.microsoft.com:80/en-us/library/bb313958.aspx "12 May 2009") | APR | [**Jul**](https://web.archive.org/web/20100705134106/http://msdn.microsoft.com:80/en-us/library/bb313958.aspx "05 Jul 2010")  
---|---|---  
[![Previous capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_prv_on.png)](https://web.archive.org/web/20090512001222/http://msdn.microsoft.com:80/en-us/library/bb313958.aspx "00:12:22 May 12, 2009") | 25 | [![Next capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_nxt_on.png)](https://web.archive.org/web/20100705134106/http://msdn.microsoft.com:80/en-us/library/bb313958.aspx "13:41:06 Jul 05, 2010")  
2009 | 2010 | 2011  
success
fail
[ ](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313958.aspx "Share via My Web Archive") [ ](https://archive.org/account/login.php "Sign In") [](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine") [](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313958.aspx#close "Close the toolbar")
[ ](https://web.archive.org/web/20100425013737/http://web.archive.org/screenshot/http://msdn.microsoft.com/en-us/library/bb313958.aspx "screenshot") [ ](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313958.aspx "video") [](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313958.aspx "Share on Facebook") [](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313958.aspx "Share on Twitter")
[About this capture](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313958.aspx#expand)
COLLECTED BY
[Alexa Crawls](https://archive.org/details/alexacrawls)
[Alexa Internet](http://www.alexa.com/) has been donating their crawl data to the Internet Archive. Flowing in every day, these data are added to the [Wayback Machine](http://web.archive.org/) after an embargo period. 
Collection: [alexa_web_2010](https://archive.org/details/alexa_web_2010)
TIMESTAMPS
![loading](https://web-static.archive.org/_static/images/loading.gif)
The Wayback Machine - https://web.archive.org/web/20100425013737/http://msdn.microsoft.com:80/en-us/library/bb313958.aspx
XNA Game Studio 3.1
tfetch3D (xvs_3_0, xps_3_0)
Fetches sample data from a 3D texture.  ```
tfetch3D dest, src1, fetchConst [, name = value, ...]
```
  
---  
# Name-Value Pair 

**UnnormalizedTextureCoords** = **bool** 
    If **UnnormalizedTextureCoords** is **true** , texture coordinates should range between 0 and the dimensions of the texture; otherwise, the texture coordinates should range beween 0.0f and 1.0f. The default value is **false**. 

**MagFilter** = **enum** 
    
Filter used when the texture is magnified. **MagFilter** must be one of the following values.
Value | Description  
---|---  
point | Point filter. The texel with coordinates nearest to the desired pixel value is used.  
linear | Bilinear interpolation filter. A weighted average of a 22 area of texels surrounding the desired pixel is used.  
keep | Use the filtering set up by Direct3D. This is the default value. 

**MinFilter** = **enum** 
      
Filter used when the texture is minified. **MinFilter** must be one of the following values.
Value | Description  
---|---  
point | Point filter. The texel with coordinates nearest to the desired pixel value is used.  
linear | Bilinear interpolation filter. A weighted average of a 22 area of texels surrounding the desired pixel is used.  
keep | Use the filtering set up by Direct3D. This is the default value. 

**MipFilter** = **enum** 
      
Filter used between mipmap levels. **MipFilter** must be one of the following values.
Value | Description  
---|---  
point | Point filter. The mipmap with coordinates nearest to the desired pixel value is used.  
linear | Trilinear interpolation filtering is used as a mipmap filter, using the texels of the two nearest mipmap textures.  
keep | Use the filtering set up by Direct3D. This is the default value. 

**VolMagFilter** = **enum** 
      
Filter used when the volume is magnified. **VolMagFilter** must be one of the following values.
Value | Description  
---|---  
point | Point filter. The texel with coordinates nearest to the desired pixel value is used.  
linear | Bilinear interpolation filter. A weighted average of a 22 area of texels surrounding the desired pixel is used.  
keep | Use the filtering set up by Direct3D. This is the default value. 

**VolMinFilter** = **enum** 
      
Filter used when the volume is minified. **VolMinFilter** must be one of the following values.
Value | Description  
---|---  
point | Point filter. The texel with coordinates nearest to the desired pixel value is used.  
linear | Bilinear interpolation filter. A weighted average of a 22 area of texels surrounding the desired pixel is used.  
keep | Use the filtering set up by Direct3D. This is the default value. 

**UseComputedLOD** = **bool** 
    If **UseComputedLOD** is **true** , the shader will use the LOD computed in the texture pipeline. The default value is **true**. For more details, see [Computing the LOD](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313958.aspx#bias). 

**UseRegisterLOD** = **bool** 
    If **UseRegisterLOD** is **true** , the shader will use the LOD set by [setTexLOD](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313955.aspx). The default value is **false**. For more details, see [Computing the LOD](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313958.aspx#bias). 

**LODBias** = **float** 
    Bias to add to the LOD. The _value_ must be a number between −4.0 and 3.9375. In addition, _value_ must be an integer multiple of 0.0625. The default value is 0.0f. For more details, see [Computing the LOD](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313958.aspx#bias). 

**OffsetX** = **float** 
    Value added to the x-component of the texel address right before sampling. The _value_ must be between −8.0f and 7.5f. In addition, _value_ must be an integer multiple of 0.5f. The default value is 0.0f.  

**OffsetY** = **float** 
     Value added to the y-component of the texel address right before sampling. The _value_ must be between −8.0f and 7.5f. In addition, _value_ must be an integer multiple of 0.5f. The default value is 0.0f. 

**OffsetZ** = **float** 
    Value added to the z-component of the texel address right before sampling. The _value_ must be between −8.0f and 7.5f. In addition, _value_ must be an integer multiple of 0.5f. The default value is 0.0f. 

**FetchValidOnly** = **bool** 
      
Performance booster that determines if pixel data should be fetched for pixels outside of the current primitive. The default value is **true**. For vertex shaders, **FetchValidOnly** should always be **true**. For pixel shaders, **FetchValidOnly** should be **true** , unless the result of the **tfetch** instruction is used to calculate a gradient, by using [getGradients](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb464129.aspx) or a **tfetch** instruction with **UseComputedLOD** set to **true**. 
Gradient information is calculated by running a 2×2 quad of pixel shaders and computing the difference between the resulting pixels. At the edges of triangles, there are situations where one or more of the pixel shaders in the quad lies outside the boundary of the triangle, and so its computed values won't be output. The **FetchValidOnly** value is used to tell the hardware that it doesn't have to fetch the pixel data for these out-of-bounds pixel shaders. When **FetchValidOnly** is **true** , data will be fetched only for those pixels that are valid (inside the triangle), which speeds up the calculations.
In cases where the result of the texture fetch is itself used to calculate gradient information, all four pixel shaders in the quad are necessary to compute the gradients, and **FetchValidOnly** should be set to **false**.
Remarks
* * *
The _src1_ register specifies the coordinates from which to fetch the sample data.
If **UnnormalizedTextureCoords** is **true** , you must set the [AddressU](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/microsoft.xna.framework.graphics.samplerstate.addressu.aspx), [AddressW](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/microsoft.xna.framework.graphics.samplerstate.addressw.aspx), and [AddressV](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/microsoft.xna.framework.graphics.samplerstate.addressv.aspx) texture sampler states to a clamping mode such as [TextureAddressMode.Clamp](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/microsoft.xna.framework.graphics.textureaddressmode.aspx#TextureAddressMode.Clamp), rather than a wrapping mode. Using a wrapping mode will force normalized texture coordinates even if **UnnormalizedTextureCoords** is **true**.
![Bb313958.note\(en-us,XNAGameStudio.31\).gif](https://web.archive.org/web/20100425013737im_/http://i.msdn.microsoft.com/Bb313958.note\(en-us,XNAGameStudio.31\).gif)Note   
---  
To use the **tfetch3D (xvs_3_0, xps_3_0)** instruction in a vertex shader, **UseComputedLOD** must be **false** unless you manually set the gradients and you set **UseRegisterGradients** to **true**.  
## Computing the LOD
The total LOD for a sample is additive and is based on what is enabled. The total LOD is determined by the LOD computed in the texture pipeline (if **UseComputedLOD** is **true**), the LOD set by [setTexLOD](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313955.aspx) (if **UseRegisterLOD** is **true**), and the **LODBias** value.
* * *
  
[MSDN Library](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/aa468128.aspx)  
[XNA Game Studio 3.1](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313961.aspx)  
[Fetch Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313942.aspx)  
[tfetch3D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425013737/http://msdn.microsoft.com/en-us/library/bb313958.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20100425013737im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

## ALU Scalar Instructions (xvs_3_0, xps_3_0)

**Source:** http%3A//msdn.microsoft.com/en-us/library/bb313879.aspx
**Word Count:** 782

[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")
[1 capture](https://web.archive.org/web/20100425014442*/http://msdn.microsoft.com/en-us/library/bb313879.aspx "See a list of every capture for this URL")
25 Apr 2010
[ ](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313879.aspx)
Mar | APR | May  
---|---|---  
![Previous capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_prv_off.png) | 25 | ![Next capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_nxt_off.png)  
2009 | 2010 | 2011  
success
fail
[ ](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313879.aspx "Share via My Web Archive") [ ](https://archive.org/account/login.php "Sign In") [](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine") [](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313879.aspx#close "Close the toolbar")
[ ](https://web.archive.org/web/20100425014442/http://web.archive.org/screenshot/http://msdn.microsoft.com/en-us/library/bb313879.aspx "screenshot") [ ](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313879.aspx "video") [](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313879.aspx "Share on Facebook") [](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313879.aspx "Share on Twitter")
[About this capture](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313879.aspx#expand)
COLLECTED BY
[Alexa Crawls](https://archive.org/details/alexacrawls)
[Alexa Internet](http://www.alexa.com/) has been donating their crawl data to the Internet Archive. Flowing in every day, these data are added to the [Wayback Machine](http://web.archive.org/) after an embargo period. 
Collection: [alexa_web_2010](https://archive.org/details/alexa_web_2010)
TIMESTAMPS
![loading](https://web-static.archive.org/_static/images/loading.gif)
The Wayback Machine - https://web.archive.org/web/20100425014442/http://msdn.microsoft.com:80/en-us/library/bb313879.aspx
XNA Game Studio 3.1
ALU Scalar Instructions (xvs_3_0, xps_3_0)
Instruction | Description  
---|---  
[adds](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313880.aspx) |  Computes the sum of the two components of the source.  
[adds_prev](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313881.aspx) |  Computes the sum of the source and the result of the previous scalar operation.  
[cos](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313882.aspx) |  Computes the cosine of the source.  
[exp](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313883.aspx) |  Computes the base-2 exponential of the source.  
[floors](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313884.aspx) |  Computes the greatest integer that is less than or equal to the source.  
[frcs](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313885.aspx) |  Computes the fractional part of the source.  
[log](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313886.aspx) |  Computes the base-2 logarithm of the source.  
[logc](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313887.aspx) |  Computes the base-2 logarithm of the source, clamped to the range −MIN_FLOAT to +MAX_FLOAT.  
[maxas](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313889.aspx) |  Updates the address register (a0) with the first component of the source register. It then computes the maximum of the two components of the source.  
[maxasf](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313890.aspx) |  Updates the address register (a0) with the first component of the source register, floored. It then computes the maximum of the two components of the source.  
[maxs](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313891.aspx) |  Computes the maximum of the two components of the source.  
[mins](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313892.aspx) |  Computes the minimum of the two components of the source.  
[movas](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313893.aspx) |  Moves scalar data between registers and updates the address register (a0) with the source register, rounded to the nearest integer.  
[movasf](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313894.aspx) |  Moves scalar data between registers and updates the address register (a0) with the source register, floored.  
[movs](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313895.aspx) |  Moves scalar data between registers.  
[muls](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313896.aspx) |  Multiplies the two specified components of the source.  
[muls_prev](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313897.aspx) |  Computes the product of the source register and the result of the previous scalar operation.  
[muls_prev2](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313898.aspx) |  Computes the product of the source register and the result of the previous scalar operation, with bounds checking.   
[nops](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313899.aspx) |  No operation is performed on the scalar ALU.  
[rcp](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313900.aspx) |  Computes the reciprocal of the source.  
[rcpc](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313901.aspx) |  Computes the reciprocal of the source, clamped to the range −MIN_FLOAT to +MAX_FLOAT.  
[rcpf](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313902.aspx) |  Computes the reciprocal of the source, mimicking the behavior of the fixed-function pipeline.  
[retain_prev](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313903.aspx) |  Returns the result of the previous scalar instruction.  
[rsq](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313904.aspx) |  Computes the reciprocal square root of the source.  
[rsqc](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313905.aspx) |  Computes the reciprocal square root of the source, clamped to the range −MIN_FLOAT to +MAX_FLOAT.  
[rsqf](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313906.aspx) |  Computes the reciprocal square root of the source, mimicking the behavior of the fixed-function pipeline.  
[seqs](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313907.aspx) |  Sets the destination components equal to one if the source is zero.  
[sges](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313908.aspx) |  Sets the destination components equal to one if the source is greater than or equal to zero.  
[sgts](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313909.aspx) |  Sets the destination components equal to one if the source is greater than zero.  
[sin](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313910.aspx) |  Computes the sine of the source.  
[snes](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313911.aspx) |  Sets the destination components equal to one if the source is nonzero.  
[sqrt](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313912.aspx) |  Computes the square root of the source.  
[subs](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313913.aspx) |  Computes the difference between the two specified components of the source.  
[subs_prev](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313914.aspx) |  Computes the difference of the source register and the result of the previous scalar operation.  
[truncs](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313915.aspx) |  Truncates the source.  
See Also
* * *
#### Concepts
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  

  
[adds (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313880.aspx)  
[adds_prev (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313881.aspx)  
[cos (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313882.aspx)  
[exp (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313883.aspx)  
[floors (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313884.aspx)  
[frcs (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313885.aspx)  
[log (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313886.aspx)  
[logc (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313887.aspx)  
[maxas (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313889.aspx)  
[maxasf (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313890.aspx)  
[maxs (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313891.aspx)  
[mins (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313892.aspx)  
[movas (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313893.aspx)  
[movasf (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313894.aspx)  
[movs (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313895.aspx)  
[muls (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313896.aspx)  
[muls_prev (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313897.aspx)  
[muls_prev2 (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313898.aspx)  
[nops (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313899.aspx)  
[rcp (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313900.aspx)  
[rcpc (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313901.aspx)  
[rcpf (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313902.aspx)  
[retain_prev (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313903.aspx)  
[rsq (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313904.aspx)  
[rsqc (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313905.aspx)  
[rsqf (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313906.aspx)  
[seqs (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313907.aspx)  
[sges (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313908.aspx)  
[sgts (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313909.aspx)  
[sin (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313910.aspx)  
[snes (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313911.aspx)  
[sqrt (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313912.aspx)  
[subs (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313913.aspx)  
[subs_prev (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313914.aspx)  
[truncs (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313915.aspx)
* * *
  
[MSDN Library](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/aa468128.aspx)  
[XNA Game Studio 3.1](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313961.aspx)  
[ALU Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313878.aspx)  
[ALU Scalar Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20100425014442/http://msdn.microsoft.com/en-us/library/bb313879.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20100425014442im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

## Fetch Instructions (xvs_3_0, xps_3_0)

**Source:** http://msdn.microsoft.com/en-us/library/bb313942.aspx
**Word Count:** 547

[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")
[2 captures](https://web.archive.org/web/20090918114559*/http://msdn.microsoft.com/en-us/library/bb313942.aspx "See a list of every capture for this URL")
10 May 2009 - 18 Sep 2009
[ ](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313942.aspx)
[**May**](https://web.archive.org/web/20090510235238/http://msdn.microsoft.com:80/en-us/library/bb313942.aspx "10 May 2009") | SEP | Oct  
---|---|---  
[![Previous capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_prv_on.png)](https://web.archive.org/web/20090510235238/http://msdn.microsoft.com:80/en-us/library/bb313942.aspx "23:52:38 May 10, 2009") | 18 | ![Next capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_nxt_off.png)  
2008 | 2009 | 2010  
success
fail
[ ](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313942.aspx "Share via My Web Archive") [ ](https://archive.org/account/login.php "Sign In") [](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine") [](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313942.aspx#close "Close the toolbar")
[ ](https://web.archive.org/web/20090918114559/http://web.archive.org/screenshot/http://msdn.microsoft.com/en-us/library/bb313942.aspx "screenshot") [ ](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313942.aspx "video") [](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313942.aspx "Share on Facebook") [](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313942.aspx "Share on Twitter")
[About this capture](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313942.aspx#expand)
COLLECTED BY
[Alexa Crawls](https://archive.org/details/alexacrawls)
[Alexa Internet](http://www.alexa.com/) has been donating their crawl data to the Internet Archive. Flowing in every day, these data are added to the [Wayback Machine](http://web.archive.org/) after an embargo period. 
Collection: [alexa_web_2009](https://archive.org/details/alexa_web_2009)
TIMESTAMPS
![loading](https://web-static.archive.org/_static/images/loading.gif)
The Wayback Machine - https://web.archive.org/web/20090918114559/http://msdn.microsoft.com:80/en-us/library/bb313942.aspx
XNA Game Studio 3.1
Fetch Instructions (xvs_3_0, xps_3_0)
Provides microcode fetch instructions. 
Instruction | Description  
---|---  
[ getBCF1D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313943.aspx) |  Gets the fraction of border color that would be blended into the texture data (retrieved using a 1D-texture fetch) at the specified coordinates.  
[ getBCF2D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313944.aspx) |  Gets the fraction of border color that would be blended into the texture data (retrieved using a 2D-texture fetch) at the specified coordinates.  
[ getBCF3D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313945.aspx) |  Gets the fraction of border color that would be blended into the texture data (retrieved using a 3D-texture fetch) at the specified coordinates.  
[ getBCFCube](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313946.aspx) |  Gets the fraction of border color that would be blended into the texture data (retrieved using a cube-texture fetch) at the specified coordinates.  
[ getCompTexLOD1D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313947.aspx) |  For 1D textures, gets the LOD for all of the pixels in the quad at the specified coordinates.  
[ getCompTexLOD2D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313948.aspx) |  For 2D textures, gets the LOD for all of the pixels in the quad at the specified coordinates.  
[ getCompTexLOD3D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313949.aspx) |  For 3D textures, gets the LOD for all of the pixels in the quad at the specified coordinates.  
[ getCompTexLODCube](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313950.aspx) |  For cube textures, gets the LOD for all of the pixels in the quad at the specified coordinates.  
[ getWeights1D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313951.aspx) |  Gets the weights used in a bilinear fetch from a 1D texture.  
[ getWeights2D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313952.aspx) |  Gets the weights used in a bilinear fetch from 2D textures.  
[ getWeights3D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313953.aspx) |  Gets the weights used in a bilinear fetch from 3D textures.  
[ getWeightsCube](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313954.aspx) |  Gets the weights used in a bilinear fetch from cube textures.  
[ setTexLOD](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313955.aspx) |  Sets the level of detail.  
[ tfetch1D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313956.aspx) |  Fetches sample data from a 1D texture.  
[ tfetch2D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313957.aspx) |  Fetches sample data from a 2D texture.  
[ tfetch3D](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313958.aspx) |  Fetches sample data from a 3D texture.  
[ tfetchCube](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313959.aspx) |  Fetches sample data from a cube texture.  
[ vfetch](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313960.aspx) |  Fetches data from a vertex buffer using a semantic.  
  
[getBCF1D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313943.aspx)  
[getBCF2D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313944.aspx)  
[getBCF3D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313945.aspx)  
[getBCFCube (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313946.aspx)  
[getCompTexLOD1D (xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313947.aspx)  
[getCompTexLOD2D (xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313948.aspx)  
[getCompTexLOD3D (xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313949.aspx)  
[getCompTexLODCube (xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313950.aspx)  
[getWeights1D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313951.aspx)  
[getWeights2D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313952.aspx)  
[getWeights3D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313953.aspx)  
[getWeightsCube (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313954.aspx)  
[setTexLOD (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313955.aspx)  
[tfetch1D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313956.aspx)  
[tfetch2D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313957.aspx)  
[tfetch3D (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313958.aspx)  
[tfetchCube (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313959.aspx)  
[vfetch (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313960.aspx)
* * *
  
[MSDN Library](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/ms123401.aspx)  
[Development Tools and Languages](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/aa187916.aspx)  
[XNA Game Studio](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/aa139594.aspx)  
[XNA Game Studio 3.1](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb200104.aspx)  
[Programming Guide](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb198548.aspx)  
[Hardware and Platforms](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb975657.aspx)  
[Xbox 360 Programming](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb417501.aspx)  
[Microcode (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313877.aspx)  
[Microcode Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313961.aspx)  
[Fetch Instructions (xvs_3_0, xps_3_0)](https://web.archive.org/web/20090918114559/http://msdn.microsoft.com/en-us/library/bb313942.aspx)
* * *
Tags: 
![](https://web.archive.org/web/20090918114559im_/http://i.msdn.microsoft.com/Global/Images/wiki.gif)
Community Content


---

## Wayback Machine

**Source:** http%3A//msdn.microsoft.com/en-us/library/bb313898.aspx
**Word Count:** 756

[Ask the publishers](https://change.org/LetReadersRead) to restore access to 500,000+ books.
Hamburger icon An icon used to represent a menu that can be toggled by interacting with this icon.
[ Internet Archive logo A line drawing of the Internet Archive headquarters building façade. ](https://archive.org/ "Go home")
[ Web icon An illustration of a computer application window Wayback Machine ](https://web.archive.org "Expand web menu") [ Texts icon An illustration of an open book.  Texts ](https://archive.org/details/texts "Expand texts menu") [ Video icon An illustration of two cells of a film strip. Video ](https://archive.org/details/movies "Expand video menu") [ Audio icon An illustration of an audio speaker.  Audio ](https://archive.org/details/audio "Expand audio menu") [ Software icon An illustration of a 3.5" floppy disk. Software ](https://archive.org/details/software "Expand software menu") [ Images icon An illustration of two photographs.  Images ](https://archive.org/details/image "Expand images menu") [ Donate icon An illustration of a heart shape  Donate ](https://archive.org/donate/ "Expand donate menu") [ Ellipses icon An illustration of text ellipses.  More ](https://archive.org/about/ "Expand more menu")
[ Donate icon An illustration of a heart shape "Donate to the archive" ](https://archive.org/donate/?origin=iawww-mbhrt)
User icon An illustration of a person's head and chest.  [Sign up](https://archive.org/account/signup) | [Log in](https://archive.org/account/login)
[ Upload icon An illustration of a horizontal line over an up pointing arrow. Upload ](https://archive.org/create) Search icon An illustration of a magnifying glass.
Search icon An illustration of a magnifying glass.
###  Internet Archive Audio
[![](https://archive.org/services/img/etree)Live Music Archive](https://archive.org/details/etree) [![](https://archive.org/services/img/librivoxaudio)Librivox Free Audio](https://archive.org/details/librivoxaudio)
#### Featured
  * [All Audio](https://archive.org/details/audio)
  * [Grateful Dead](https://archive.org/details/GratefulDead)
  * [Netlabels](https://archive.org/details/netlabels)
  * [Old Time Radio](https://archive.org/details/oldtimeradio)
  * [78 RPMs and Cylinder Recordings](https://archive.org/details/78rpm)


#### Top
  * [Audio Books & Poetry](https://archive.org/details/audio_bookspoetry)
  * [Computers, Technology and Science](https://archive.org/details/audio_tech)
  * [Music, Arts & Culture](https://archive.org/details/audio_music)
  * [News & Public Affairs](https://archive.org/details/audio_news)
  * [Spirituality & Religion](https://archive.org/details/audio_religion)
  * [Podcasts](https://archive.org/details/podcasts)
  * [Radio News Archive](https://archive.org/details/radio)


###  Images
[![](https://archive.org/services/img/metropolitanmuseumofart-gallery)Metropolitan Museum](https://archive.org/details/metropolitanmuseumofart-gallery) [![](https://archive.org/services/img/clevelandart)Cleveland Museum of Art](https://archive.org/details/clevelandart)
#### Featured
  * [All Images](https://archive.org/details/image)
  * [Flickr Commons](https://archive.org/details/flickrcommons)
  * [Occupy Wall Street Flickr](https://archive.org/details/flickr-ows)
  * [Cover Art](https://archive.org/details/coverartarchive)
  * [USGS Maps](https://archive.org/details/maps_usgs)


#### Top
  * [NASA Images](https://archive.org/details/nasa)
  * [Solar System Collection](https://archive.org/details/solarsystemcollection)
  * [Ames Research Center](https://archive.org/details/amesresearchcenterimagelibrary)


###  Software
[![](https://archive.org/services/img/internetarcade)Internet Arcade](https://archive.org/details/internetarcade) [![](https://archive.org/services/img/consolelivingroom)Console Living Room](https://archive.org/details/consolelivingroom)
#### Featured
  * [All Software](https://archive.org/details/software)
  * [Old School Emulation](https://archive.org/details/tosec)
  * [MS-DOS Games](https://archive.org/details/softwarelibrary_msdos_games)
  * [Historical Software](https://archive.org/details/historicalsoftware)
  * [Classic PC Games](https://archive.org/details/classicpcgames)
  * [Software Library](https://archive.org/details/softwarelibrary)


#### Top
  * [Kodi Archive and Support File](https://archive.org/details/kodi_archive)
  * [Vintage Software](https://archive.org/details/vintagesoftware)
  * [APK](https://archive.org/details/apkarchive)
  * [MS-DOS](https://archive.org/details/softwarelibrary_msdos)
  * [CD-ROM Software](https://archive.org/details/cd-roms)
  * [CD-ROM Software Library](https://archive.org/details/cdromsoftware)
  * [Software Sites](https://archive.org/details/softwaresites)
  * [Tucows Software Library](https://archive.org/details/tucows)
  * [Shareware CD-ROMs](https://archive.org/details/cdbbsarchive)
  * [Software Capsules Compilation](https://archive.org/details/softwarecapsules)
  * [CD-ROM Images](https://archive.org/details/cdromimages)
  * [ZX Spectrum](https://archive.org/details/softwarelibrary_zx_spectrum)
  * [DOOM Level CD](https://archive.org/details/doom-cds)


###  Texts
[![](https://archive.org/images/widgetOL.png)Open Library](https://openlibrary.org/) [![](https://archive.org/services/img/americana)American Libraries](https://archive.org/details/americana)
#### Featured
  * [All Texts](https://archive.org/details/texts)
  * [Smithsonian Libraries](https://archive.org/details/smithsonian)
  * [FEDLINK (US)](https://archive.org/details/fedlink)
  * [Genealogy](https://archive.org/details/genealogy)
  * [Lincoln Collection](https://archive.org/details/lincolncollection)


#### Top
  * [American Libraries](https://archive.org/details/americana)
  * [Canadian Libraries](https://archive.org/details/toronto)
  * [Universal Library](https://archive.org/details/universallibrary)
  * [Project Gutenberg](https://archive.org/details/gutenberg)
  * [Children's Library](https://archive.org/details/iacl)
  * [Biodiversity Heritage Library](https://archive.org/details/biodiversity)
  * [Books by Language](https://archive.org/details/booksbylanguage)
  * [Additional Collections](https://archive.org/details/additional_collections)


###  Video
[![](https://archive.org/services/img/tv)TV News](https://archive.org/details/tv) [![](https://archive.org/services/img/911)Understanding 9/11](https://archive.org/details/911)
#### Featured
  * [All Video](https://archive.org/details/movies)
  * [Prelinger Archives](https://archive.org/details/prelinger)
  * [Democracy Now!](https://archive.org/details/democracy_now_vid)
  * [Occupy Wall Street](https://archive.org/details/occupywallstreet)
  * [TV NSA Clip Library](https://archive.org/details/nsa)


#### Top
  * [Animation & Cartoons](https://archive.org/details/animationandcartoons)
  * [Arts & Music](https://archive.org/details/artsandmusicvideos)
  * [Computers & Technology](https://archive.org/details/computersandtechvideos)
  * [Cultural & Academic Films](https://archive.org/details/culturalandacademicfilms)
  * [Ephemeral Films](https://archive.org/details/ephemera)
  * [Movies](https://archive.org/details/moviesandfilms)
  * [News & Public Affairs](https://archive.org/details/newsandpublicaffairs)
  * [Spirituality & Religion](https://archive.org/details/spiritualityandreligion)
  * [Sports Videos](https://archive.org/details/sports)
  * [Television](https://archive.org/details/television)
  * [Videogame Videos](https://archive.org/details/gamevideos)
  * [Vlogs](https://archive.org/details/vlogs)
  * [Youth Media](https://archive.org/details/youth_media)


Search the history of over __WB_PAGES_ARCHIVED__ [web pages](https://blog.archive.org/2016/10/23/defining-web-pages-web-sites-and-web-captures/) on the Internet. 
[ ](https://web.archive.org) Search the Wayback Machine
Search icon An illustration of a magnifying glass.
#### Mobile Apps
  * [Wayback Machine (iOS)](https://apps.apple.com/us/app/wayback-machine/id1201888313)
  * [Wayback Machine (Android)](https://play.google.com/store/apps/details?id=com.archive.waybackmachine&hl=en_US)


#### Browser Extensions
  * [Chrome](https://chrome.google.com/webstore/detail/wayback-machine/fpnmgdkabkmnadcjpehmlllkndpkmiak)
  * [Firefox](https://addons.mozilla.org/en-US/firefox/addon/wayback-machine_new/)
  * [Safari](https://apps.apple.com/us/app/wayback-machine/id1472432422?mt=12)
  * [Edge](https://microsoftedge.microsoft.com/addons/detail/wayback-machine/kjmickeoogghaimmomagaghnogelpcpn?hl=en-US)


#### Archive-It Subscription
  * [Explore the Collections](https://www.archive-it.org/explore)
  * [Learn More](https://www.archive-it.org/blog/learn-more/)
  * [Build Collections](https://www.archive-it.org/contact-us)


### Save Page Now
Capture a web page as it appears now for use as a trusted citation in the future.
Please enter a valid web address
  * [About](https://archive.org/about/)
  * [Blog](https://blog.archive.org)
  * [Projects](https://archive.org/projects/)
  * [Help](https://archive.org/about/faqs.php)
  * [Donate](https://archive.org/donate?origin=iawww-TopNavDonateButton)
  * [Contact](https://archive.org/about/contact)
  * [Jobs](https://archive.org/about/jobs)
  * [Volunteer](https://archive.org/about/volunteer-positions)
  * [People](https://archive.org/about/bios)


  * [ Sign up for free  ](https://archive.org/account/signup)
  * [ Log in  ](https://archive.org/account/login)


Search metadata  Search text contents  Search TV news captions  Search radio transcripts  Search archived web sites  [Advanced Search](https://archive.org/advancedsearch.php)
  * [About](https://archive.org/about/)
  * [Blog](https://blog.archive.org)
  * [Projects](https://archive.org/projects/)
  * [Help](https://archive.org/about/faqs.php)
  * [Donate Donate icon An illustration of a heart shape ](https://archive.org/donate?origin=iawww-TopNavDonateButton)
  * [Contact](https://archive.org/about/contact)
  * [Jobs](https://archive.org/about/jobs)
  * [Volunteer](https://archive.org/about/volunteer-positions)
  * [People](https://archive.org/about/bios)


[DONATE](http://archive.org/donate/?origin=wbwww-CalndrDonateButton)
[](https://web.archive.org/)
Latest Show All
## Hrm.
The Wayback Machine has not archived that URL.
Click here to search for all archived pages under [http://msdn.microsoft.com/en-us/library/](https://web.archive.org/web/*/http://msdn.microsoft.com/en-us/library/*). 
The Wayback Machine is an initiative of the [Internet Archive](https://archive.org/), a 501(c)(3) non-profit, building a digital library of Internet sites and other cultural artifacts in digital form.   
Other [projects](https://archive.org/projects/) include [Open Library](https://openlibrary.org/) & [archive-it.org](https://archive-it.org). 
Your use of the Wayback Machine is subject to the Internet Archive's [Terms of Use](https://archive.org/about/terms.php). 


---

## Removed Content

**Source:** http://msdn.microsoft.com/en-us/library/bb313880.aspx
**Word Count:** 408

[![Wayback Machine](https://web-static.archive.org/_static/images/toolbar/wayback-toolbar-logo-200.png)](https://web.archive.org/web/ "Wayback Machine home page")
[1 capture](https://web.archive.org/web/20120423040154*/http://msdn.microsoft.com/en-us/library/bb313880.aspx "See a list of every capture for this URL")
23 Apr 2012
[ ](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/bb313880.aspx)
Mar | APR | May  
---|---|---  
![Previous capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_prv_off.png) | 23 | ![Next capture](https://web-static.archive.org/_static/images/toolbar/wm_tb_nxt_off.png)  
2011 | 2012 | 2013  
success
fail
[ ](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/bb313880.aspx "Share via My Web Archive") [ ](https://archive.org/account/login.php "Sign In") [](https://help.archive.org/help/category/the-wayback-machine/ "Get some help using the Wayback Machine") [](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/bb313880.aspx#close "Close the toolbar")
[ ](https://web.archive.org/web/20120423040154/http://web.archive.org/screenshot/http://msdn.microsoft.com/en-us/library/bb313880.aspx "screenshot") [ ](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/bb313880.aspx "video") [](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/bb313880.aspx "Share on Facebook") [](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/bb313880.aspx "Share on Twitter")
[About this capture](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/bb313880.aspx#expand)
COLLECTED BY
[Internet Archive](https://archive.org/details/webwidecrawl)
[Wayback Machine](http://archive.org/web/web.php). 
Collection: [Live Web Proxy Crawls](https://archive.org/details/liveweb)
[Wayback Machine](http://archive.org/web/web.php) Live Proxy mostly by the Save Page Now feature on web.archive.org.   
  
Liveweb proxy is a component of Internet Archive’s wayback machine project. The liveweb proxy captures the content of a web page in real time, archives it into a ARC or WARC file and returns the ARC/WARC record back to the wayback machine to process. The recorded ARC/WARC file becomes part of the wayback machine in due course of time.   

TIMESTAMPS
![loading](https://web-static.archive.org/_static/images/loading.gif)
The Wayback Machine - https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/bb313880.aspx
[Home](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/default.aspx "Home") [Library](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/default.aspx "Library") [Learn](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/bb188199.aspx "Learn") [Downloads](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/aa570309.aspx "Downloads") [Support](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/hh361695.aspx "Support") [Community](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/aa497440.aspx "Community") |  [Sign in ](https://web.archive.org/web/20120423040154/https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=11&ct=1335153715&rver=6.0.5276.0&wp=MCLBI&wlcxt=msdn%24msdn%24msdn&wreply=http%3a%2f%2fmsdn.microsoft.com%2fen-us%2flibrary%2fbb313880.aspx&lc=1033&id=254354&mkt=en-US "Sign in") | [United States - English ](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/preferences/locale/?returnurl=%252fen-us%252flibrary%252fbb313880.aspx "United States - English") | [![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/preferences/experience/?returnurl=%252fen-us%252flibrary%252fbb313880.aspx "Preferences") | [![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/bb313880\(d=printer\).aspx "Print/Export") [![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)](javascript:void\(0\); "Print/Export")  
---|---  
|   
---|---  
![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[MSDN Library](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/ms123401.aspx "MSDN Library")
![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Design Tools](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/cc295789.aspx "Design Tools")
![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Development Tools and Languages](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/aa187916.aspx "Development Tools and Languages")
![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Mobile and Embedded Development](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/ms376734.aspx "Mobile and Embedded Development")
![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[.NET Development](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/ff361664\(v=vs.110\).aspx ".NET Development")
![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Office Development](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/bb726434\(v=office.12\).aspx "Office Development")
![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Online Services](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/ee702802.aspx "Online Services")
![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Open Specifications](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/dd208104\(v=prot.10\).aspx "Open Specifications")
![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[patterns & practices](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/ff921345.aspx "patterns & practices")
![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Servers and Enterprise Development](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/aa155072.aspx "Servers and Enterprise Development")
![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Speech Technologies](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/hh323806.aspx "Speech Technologies")
![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Web Development](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/aa155073.aspx "Web Development")
![](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png)
[Windows Development](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/ee663300\(v=vs.85\).aspx "Windows Development")
![Separator](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Global/Content/clear.gif)
[ ![Expand](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png) ![Minimize](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png) ](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/bb313880.aspx)
[ ![MSDN](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png) ](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/default.aspx)
This topic has not yet been rated [- Rate this topic](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/en-us/library/bb313880.aspx#feedback "Rate this topic")
# Removed Content
This content has been removed, but may be available in the product documentation installed on your computer.
Did you find this helpful? Yes No
Not accurate
Not enough depth
Need more code examples
Tell us more...
(1500 characters remaining)
© 2012 Microsoft. All rights reserved.
[Terms of Use](https://web.archive.org/web/20120423040154/http://msdn.microsoft.com/cc300389.aspx) |  [Trademarks](https://web.archive.org/web/20120423040154/http://www.microsoft.com/library/toolbar/3.0/trademarks/en-us.mspx) |  [Privacy Statement](https://web.archive.org/web/20120423040154/http://www.microsoft.com/info/privacy.mspx) |  Site Feedback [ Site Feedback  ![Site Feedback](https://web.archive.org/web/20120423040154im_/http://i.msdn.microsoft.com/Areas/Brand/Content/Msdn_ImageSprite.png) ](https://web.archive.org/web/20120423040154/http://social.msdn.microsoft.com/Forums/en-US/libraryfeedback/threads "Site Feedback")
Site Feedback
[x](javascript:;)
Tell us about your experience... 
Did the page load quickly? 
Yes No
Do you like the page design? 
Yes No
Tell us more 
Enter description here.


---

